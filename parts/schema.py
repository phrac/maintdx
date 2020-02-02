import graphene
from graphene_django import DjangoObjectType
from graphene_django.filter import DjangoFilterConnectionField
import django_filters
import maintdx.parts.models as parts

class PartInventoryItemNode(DjangoObjectType):
    class Meta:
        model = parts.PartInventoryItem
        filter_fields = {
            'part__id': ['exact'],
            'part__part_number': ['exact', 'icontains', 'istartswith'],
            'current_on_hand': ['exact', 'gt', 'lt', 'gte', 'lte'],
        }
        interfaces = (graphene.relay.Node, )

class PartNode(DjangoObjectType):
    class Meta:
        model = parts.Part
        exclude = ['image']
        filter_fields = {
            'reorder_point': ['gt', 'lt', 'gte', 'lte'],
            'part_number': ['exact', 'icontains', 'istartswith'],
            'description': ['icontains'],
            'on_hand': ['exact', 'gt', 'lt', 'gte', 'lte']
        }
        interfaces = (graphene.relay.Node, )

class PartVendorNode(DjangoObjectType):
    class Meta:
        model = parts.PartVendor
        filter_fields = {
            'part__id': ['exact'],
            'part__part_number': ['exact', 'icontains', 'istartswith'],
            'vendor__id': ['exact'],
            'vendor__name': ['exact', 'istartswith']
        }
        interfaces = (graphene.relay.Node, )

class InventoryLocationNode(DjangoObjectType):
    class Meta:
        model = parts.InventoryLocation
        filter_fields = {
            'code': ['exact', 'istartswith'],
            'description': ['exact', 'istartswith', 'icontains']
        }
        interfaces = (graphene.relay.Node, )

class Query(graphene.ObjectType):
    all_parts = DjangoFilterConnectionField(PartNode)
    all_part_vendors = DjangoFilterConnectionField(PartVendorNode)
    all_inventory_locations = DjangoFilterConnectionField(InventoryLocationNode)
    all_part_inventory_items = DjangoFilterConnectionField(PartInventoryItemNode)

    part = graphene.Node.Field(PartNode)
    part_vendor = graphene.Node.Field(PartVendorNode)
    inventory_location = graphene.Node.Field(InventoryLocationNode)
    part_inventory_item = graphene.Node.Field(PartInventoryItemNode)
