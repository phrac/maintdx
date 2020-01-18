from django.db import models

class Vendor(models.Model):
    name = models.CharField(max_length=32)
    website = models.URLField()

    def __str__(self):
        return self.name

class VendorContact(models.Model):
    name = models.CharField(max_length=32)
    title = models.CharField(max_length=32)
    email = models.EmailField()
    vendor = models.ForeignKey(Vendor)
    business_card = models.ImageField(upload_to='business_cards/')

    def __str__(self):
        return "%s @ %s" % (self.name, self.vendor.name)
