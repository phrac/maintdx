from django.contrib import admin
from maintdx.assets.models import (
    Asset,
    AssetGroup,
    Category,
    CategoryProperty,
    Location,
    Department,
)

admin.site.register(Asset)
admin.site.register(AssetGroup)
admin.site.register(Category)
admin.site.register(CategoryProperty)
admin.site.register(Location)
admin.site.register(Department)
