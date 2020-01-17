from django.db import models
from django.contrib.postgres.fields import HStoreField
from maintdx.parts.models import Part

class Category(models.Model):
    name = models.CharField(max_length=64)

    class Meta:
        verbose_name_plural = 'Categories'

    def __str__(self):
        return self.name

class CategoryProperty(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    key_name = models.CharField(max_length=32)
    required = models.BooleanField(default=True)

    class Meta:
        unique_together = ('category', 'key_name')
        verbose_name_plural = 'Category Properties'

    def save(self, *args, **kwargs):
        self.key_name = self.key_name.upper()
        super(CategoryProperty, self).save(*args, **kwargs)

        # apply new required keys to assets
        # TODO: put this in a celery task or other background
        assets = Asset.objects.filter(category=self.category)
        for a in assets:
            a.save()

    def __str__(self):
        return "%s: %s" % (self.category.name, self.key_name)

class Department(models.Model):
    name = models.CharField(max_length=64)

    def __str__(self):
        return self.name

class Location(models.Model):
    name = models.CharField(max_length=64)

    def __str__(self):
        return self.name


class Asset(models.Model):
    name = models.CharField(max_length=64)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    parent = models.ForeignKey('self', null=True, blank=True, on_delete=models.CASCADE)
    location = models.ForeignKey(Location, on_delete=models.CASCADE)
    department = models.ForeignKey(Department, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='asset_images/', null=True, blank=True)
    serial_number = models.CharField(max_length=64, null=True)
    make = models.CharField(max_length=64)
    model = models.CharField(max_length=64)
    install_date = models.DateTimeField()
    parts = models.ManyToManyField(Part)
    properties = HStoreField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        required_keys = CategoryProperty.objects.filter(
            category=self.category, required=True)

        for k in required_keys:
            if k.key_name not in self.properties.keys():
                self.properties[k.key_name] = None

        super(Asset, self).save(*args, **kwargs)

class AssetAttachment(models.Model):
    asset = models.ForeignKey(Asset, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    description = models.CharField(max_length=128)
    attachment = models.FileField(upload_to='asset_attachments/')

    def __str__(self):
        return self.description
