import graphene
from graphene_django.types import DjangoObjectType
import maintdx.parts.models as parts


class PartInventoryItemType(DjangoObjectType):
    class Meta:
        model = parts.PartInventoryItem

class PartType(DjangoObjectType):
    class Meta:
        model = parts.Part

    on_hand = graphene.Int()
    on_hand_locations = graphene.List(PartInventoryItemType)

    def resolve_on_hand(self, info):
        return self.get_on_hand_quantity()

    def resolve_on_hand_locations(self, info):
        return self.get_on_hand_locations()

class PartVendorType(DjangoObjectType):
    class Meta:
        model = parts.PartVendor

class InventoryLocationType(DjangoObjectType):
    class Meta:
        model = parts.InventoryLocation

class Query(object):
    all_parts = graphene.List(PartType)
    all_part_vendors = graphene.List(PartVendorType)
    all_inventory_locations = graphene.List(InventoryLocationType)
    all_part_inventory_items = graphene.List(PartInventoryItemType)

    part = graphene.Field(PartType, part_id=graphene.Int())
    part_vendor = graphene.Field(PartVendorType, vendor_id=graphene.Int())
    inventory_location = graphene.Field(InventoryLocationType, invloc_id=graphene.Int())
    part_inventory_item = graphene.Field(PartInventoryItemType, pii_id=graphene.Int())

    def resolve_all_parts(self, info, **kwargs):
        return parts.Part.objects.all()

    def resolve_all_part_vendors(self, info, **kwargs):
        return parts.PartVendor.objects.all()

    def resolve_all_inventory_locations(self, info, **kwargs):
        return parts.InventoryLocation.objects.all()

    def resolve_all_part_inventory_items(self, info, **kwargs):
        return parts.Part.objects.all()

    def resolve_part(self, info, part_id):
        return parts.Part.objects.get(pk=part_id)

    def resolve_part_vendor(self, info, partvendor_id):
        return parts.PartVendor.objects.get(pk=partvendor_id)

    def resolve_inventory_location(self, info, invloc_id):
        return parts.InventoryLocation.objects.get(pk=invloc_id)

    def resolve_part_inventory_item(self, info, pii_id):
        return parts.PartInventoryItem.objects.get(pk=pii_id)
