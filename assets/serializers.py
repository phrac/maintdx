from maintdx.assets.models import Asset, Category, Department, Location
from rest_framework import serializers

class AssetSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Asset
        fields = ['name', 'category', 'parent', 'location', 'department',
                  'serial_number', 'make', 'model', 'install_date', 'parts',
                  'properties']

class CategorySerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Category
        fields = ['name']

class LocationSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Location
        fields = ['name']

class DepartmentSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Department
        fields = ['name']
