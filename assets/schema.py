import graphene
from graphene_django.types import DjangoObjectType
import maintdx.assets.models as assets


class CategoryType(DjangoObjectType):
    class Meta:
        model = assets.Category

class AssetType(DjangoObjectType):
    class Meta:
        model = assets.Asset

class DepartmentType(DjangoObjectType):
    class Meta:
        model = assets.Department

class LocationType(DjangoObjectType):
    class Meta:
        model = assets.Location


class Query(object):
    all_categories = graphene.List(CategoryType)
    all_assets = graphene.List(AssetType)
    all_departments = graphene.List(DepartmentType)
    all_locations = graphene.List(LocationType)

    asset = graphene.Field(AssetType, asset_id=graphene.Int())
    category = graphene.Field(CategoryType, category_id=graphene.Int())
    department = graphene.Field(DepartmentType, department_id=graphene.Int())
    location = graphene.Field(LocationType, location_id=graphene.Int())

    def resolve_all_categories(self, info, **kwargs):
        return assets.Category.objects.all()

    def resolve_all_departments(self, info, **kwargs):
        return assets.Department.objects.all()

    def resolve_all_locations(self, info, **kwargs):
        return assets.Location.objects.all()

    def resolve_all_assets(self, info, **kwargs):
        return assets.Asset.objects.select_related('category').select_related('department').all()

    def resolve_asset(self, info, asset_id):
        return assets.Asset.objects.get(pk=asset_id)

    def resolve_category(self, info, category_id):
        return assets.Category.objects.get(pk=category_id)

    def resolve_department(self, info, department_id):
        return assets.Department.objects.get(pk=department_id)

    def resolve_location(self, info, location_id):
        return assets.Location.objects.get(pk=location_id)
