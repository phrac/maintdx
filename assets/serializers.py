from maintdx.assets import models as am
from maintdx.workorders.serializers import WorkOrderSerializer
from rest_framework import serializers

class AssetSerializer(serializers.HyperlinkedModelSerializer):
    work_orders = WorkOrderSerializer(many=True)
    class Meta:
        model = am.Asset
        fields = ['name', 'category', 'parent', 'department',
                  'serial_number', 'make', 'model', 'install_date', 'parts',
                  'properties', 'work_orders']
        depth = 1

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
        depth = 1

class DepartmentSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = am.Department
        fields = ['name', 'location']
