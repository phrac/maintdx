from maintdx.assets import models as am
from rest_framework import serializers

class AssetSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = am.Asset
        fields = ['name', 'category', 'parent', 'department',
                  'serial_number', 'make', 'model', 'install_date', 'parts',
                  'properties']

class CategorySerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = am.Category
        fields = ['name']

class CategoryPropertySerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = am.CategoryProperty
        fields = ['category', 'key_name', 'required']

class LocationSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = am.Location
        fields = ['name']

class DepartmentSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = am.Department
        fields = ['name', 'location']
