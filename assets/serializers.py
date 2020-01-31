from maintdx.assets import models as assets
from django.conf import settings
from maintdx.parts.serializers import PartSerializer
from rest_framework import serializers

class AssetSerializer(serializers.HyperlinkedModelSerializer):
    parts = PartSerializer(many=True)
    class Meta:
        model = assets.Asset
        fields = ['id', 'url', 'name', 'category', 'parent', 'department',
                  'serial_number', 'make', 'model', 'install_date', 'parts',
                  'properties', 'image']
        depth = 1

class CategorySerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = assets.Category
        fields = ['name']

class CategoryPropertySerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = assets.CategoryProperty
        fields = ['category', 'key_name', 'required']

class LocationSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = assets.Location
        fields = ['name']
        depth = 1

class DepartmentSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = assets.Department
        fields = ['name', 'location']
