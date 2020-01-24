from django.db import models
from django.contrib.auth.models import User
from maintdx.vendors.models import Vendor
from maintdx.assets.models import Department


class Part(models.Model):
    part_number = models.CharField(max_length=32)
    description = models.CharField(max_length=256)
    image = models.ImageField(upload_to='part_images/')
    reorder_point = models.IntegerField(default=0)
    max_on_hand = models.IntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE)

    def get_on_hand_quanity(self):
        items = PartInventoryItem.objects.filter(part=self)
        for i in items:
            q += i.current_on_hand
        return q

    def consume_part(self, quantity=0):
        p = PartInventoryItem.objects.filter(part=self).order_by(purchase_date)
        p.current_on_hand = p.current_on_hand - quantity
        p.save()

    def __str__(self):
        return "%s: %s" % (self.part_number, self.description)

class PartVendor(models.Model):
    part = models.ForeignKey(Part, on_delete=models.CASCADE)
    vendor = models.ForeignKey(Vendor, null=True, on_delete=models.CASCADE)
    url = models.URLField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return "%s: %s" % (self.vendor.name, self.part.part_number)

class InventoryLocation(models.Model):
    code = models.CharField(max_length=16)
    description = models.CharField(max_length=256)
    department = models.ForeignKey(Department, on_delete=models.CASCADE)

class PartInventoryItem(models.Model):
    part = model.ForeignKey(Part, on_delete=models.CASCADE)
    purchase_price = models.DecimalField(max_digits=5, decimal_places=2)
    vendor = models.ForeignKey(PartVendor, on_delete=models.CASCADE)
    purchase_date = models.DateTimeField(auto_now_add=True)
    purchase_quantity = models.IntegerField(default=0)
    current_on_hand = models.IntegerField(default=0)
    purchase_order_number = models.CharField(max_length=32)
    inventory_location = models.ForeignKey(InventoryLocation, on_delete=models.CASCADE)

