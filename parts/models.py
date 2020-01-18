from django.db import models
from maintdx.vendors.models import Vendor


class Part(models.Model):
    part_number = models.CharField(max_length=32)
    description = models.CharField(max_length=256)
    image = models.ImageField(upload_to='part_images/')
    on_hand = models.IntegerField(default=0)
    reorder_point = models.IntegerField(default=0)
    max_on_hand = models.IntegerField(default=0)
    stocking_cost = models.DecimalField(default=0, max_digits=6, decimal_places=2)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return "%s: %s" % (self.part_number, self.description)

class PartVendor(models.Model):
    part = models.ForeignKey(Part, on_delete=models.CASCADE)
    vendor = models.ForeignKey('Vendor', on_delete=models.CASCADE)
    url = models.URLField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return "%s: %s" % (self.vendor.name, self.part.part_number)
