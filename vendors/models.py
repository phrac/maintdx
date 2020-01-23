from django.db import models
from django.contrib.auth.models import User

class VendorType(models.Model):
    vendor_type = models.CharField(max_length=16)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.type

class Vendor(models.Model):
    name = models.CharField(max_length=32)
    vendor_type = models.ForeignKey(VendorType, on_delete=models.CASCADE)
    website = models.URLField()
    created_by = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

class VendorContact(models.Model):
    name = models.CharField(max_length=32)
    title = models.CharField(max_length=32)
    email = models.EmailField()
    vendor = models.ForeignKey(Vendor, on_delete=models.CASCADE)
    business_card = models.ImageField(upload_to='business_cards/')
    created_by = models.ForeignKey(User, on_delete=models.CASCADE)

    class Meta:
        unique_together = ('name', 'vendor')

    def __str__(self):
        return "%s @ %s" % (self.name, self.vendor.name)
