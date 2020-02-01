import graphene
from graphene_django.types import DjangoObjectType
from maintdx.assets.models import Asset, Category, Location, Department


class CategoryType(DjangoObjectType):
    class Meta:
        model = Category

class AssetType(DjangoObjectType):
    class Meta:
        model = Asset

class DepartmentType(DjangoObjectType):
    class Meta:
        model = Department

class LocationType(DjangoObjectType):
    class Meta:
        model = Location


class Query(object):
    all_categories = graphene.List(CategoryType)
    all_assets = graphene.List(AssetType)
    all_departments = graphene.List(DepartmentType)
    all_locations = graphene.List(LocationType)

    asset = graphene.Field(AssetType, asset_id=graphene.String())
   
    def resolve_all_categories(self, info, **kwargs):
        return Category.objects.all()

    def resolve_all_departments(self, info, **kwargs):
        return Department.objects.all()

    def resolve_all_locations(self, info, **kwargs):
        return Location.objects.all()

    def resolve_all_assets(self, info, **kwargs):
        # We can easily optimize query count in the resolve method
        return Asset.objects.select_related('category').select_related('department').all()

    def resolve_asset(self, info, asset_id):
        # Querying a single question
        return Asset.objects.get(pk=asset_id)
