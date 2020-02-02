import graphene
from graphene_django import DjangoObjectType
from graphene_django.filter import DjangoFilterConnectionField
import django_filters
import maintdx.assets.models as assets

class CategoryNode(DjangoObjectType):
    class Meta:
        model = assets.Category
        filter_fields = {
            'name': ['exact', 'istartswith', 'icontains'],
        }
        interfaces = (graphene.relay.Node, )

class LocationNode(DjangoObjectType):
    class Meta:
        model = assets.Location
        filter_fields = {
            'name': ['exact', 'istartswith', 'icontains'],
        }
        interfaces = (graphene.relay.Node, )

class DepartmentNode(DjangoObjectType):
    class Meta:
        model = assets.Department
        filter_fields = {
            'name': ['exact', 'istartswith', 'icontains'],
            'location__id': ['exact'],
            'location__name': ['exact', 'istartswith', 'icontains'],
        }
        interfaces = (graphene.relay.Node, )

class AssetNode(DjangoObjectType):
    class Meta:
        model = assets.Asset
        filter_fields = {
            'name': ['exact', 'istartswith', 'icontains'],
            'description': ['exact', 'istartswith', 'icontains'],
            'category__id': ['exact'],
            'category__name': ['exact', 'istartswith', 'icontains'],
            'parent__id': ['exact'],
            'department__id': ['exact'],
            'department__name': ['exact', 'istartswith', 'icontains'],
            'serial_number': ['exact', 'istartswith', 'icontains'],
            'make': ['exact', 'istartswith', 'icontains'],
            'model': ['exact', 'istartswith', 'icontains'],
        }
        interfaces = (graphene.relay.Node, )

class AssetAttachmentNode(DjangoObjectType):
    class Meta:
        model = assets.AssetAttachment
        filter_fields = {
            'asset__id': ['exact'],
            'asset__name': ['exact', 'istartswith', 'icontains']
        }
        interfaces = (graphene.relay.Node, )

class Query(graphene.ObjectType):
    all_categories = DjangoFilterConnectionField(CategoryNode)
    all_locations = DjangoFilterConnectionField(LocationNode)
    all_departments = DjangoFilterConnectionField(DepartmentNode)
    all_assets = DjangoFilterConnectionField(AssetNode)
    all_asset_attachments = DjangoFilterConnectionField(AssetAttachmentNode)

    category = graphene.Node.Field(CategoryNode)
    location = graphene.Node.Field(LocationNode)
    department = graphene.Node.Field(DepartmentNode)
    asset = graphene.Node.Field(AssetNode)
    asset_attachment = graphene.Node.Field(AssetAttachmentNode)
