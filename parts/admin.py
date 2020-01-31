from django.contrib import admin

from maintdx.parts.models import Part, PartVendor, PartInventoryItem, InventoryLocation

admin.site.register(Part)
admin.site.register(PartVendor)
admin.site.register(PartInventoryItem)
admin.site.register(InventoryLocation)
