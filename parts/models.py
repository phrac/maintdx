from django.db import models
from django.contrib.auth.models import User
from maintdx.vendors.models import Vendor

class Part(models.Model):
    part_number = models.CharField(max_length=32)
    description = models.CharField(max_length=256)
    image = models.ImageField(upload_to='part_images/', null=True, blank=True)
    on_hand = models.IntegerField(default=0)
    reorder_point = models.IntegerField(default=0)
    max_on_hand = models.IntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE)

    def update_on_hand_quantity(self):
        agg = PartInventoryItem.objects.filter(part=self).aggregate(models.Sum('current_on_hand'))
        count = agg['current_on_hand__sum']
        if count is None:
            count = 0
        self.on_hand = count
        self.save()

    def get_on_hand_locations(self):
        return PartInventoryItem.objects.filter(part=self, current_on_hand__gt=0)

    def consume_part(self, quantity=0):
        p = PartInventoryItem.objects.get(part=self, current_on_hand__gt=0).order_by(purchase_date)
        p.current_on_hand = p.current_on_hand - quantity
        p.save()
        self.on_hand = self.update_on_hand_quantity()
        self.save()
       
    def __str__(self):
        return "%s: %s" % (self.part_number, self.description)

class PartVendor(models.Model):
    part = models.ForeignKey(Part, on_delete=models.CASCADE)
    vendor = models.ForeignKey(Vendor, null=True, on_delete=models.CASCADE)
    url = models.URLField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return "%s: %s" % (self.vendor.name, self.part.part_number)

class InventoryLocation(models.Model):
    code = models.CharField(max_length=16)
    description = models.CharField(max_length=256)

    def __str__(self):
        return "%s: %s" % (self.code, self.description)

class PartInventoryItem(models.Model):
    part = models.ForeignKey(Part, on_delete=models.CASCADE)
    purchase_price = models.DecimalField(max_digits=5, decimal_places=2)
    vendor = models.ForeignKey(PartVendor, on_delete=models.CASCADE)
    purchase_date = models.DateTimeField(auto_now_add=True)
    purchase_quantity = models.IntegerField(default=0)
    current_on_hand = models.IntegerField(default=0)
    purchase_order_number = models.CharField(max_length=32)
    inventory_location = models.ForeignKey(InventoryLocation, on_delete=models.CASCADE)

    def save(self, *args, **kwargs):
        super(PartInventoryItem, self).save(*args, **kwargs)
        self.part.update_on_hand_quantity()
