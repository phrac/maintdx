from django.contrib import admin
from maintdx.vendors.models import Vendor, VendorContact, VendorType

admin.site.register(Vendor)
admin.site.register(VendorType)
admin.site.register(VendorContact)
