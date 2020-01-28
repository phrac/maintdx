from maintdx.assets import models as am
from django.conf import settings
from maintdx.workorders.serializers import WorkOrderSerializer
from rest_framework import serializers

class AssetSerializer(serializers.HyperlinkedModelSerializer):
    image_url = serializers.SerializerMethodField('get_image_url')

    def get_image_url(self, obj):
        r = None
        try:
            r = settings.DEV_HOST + obj.image.url
        except:
            r = None
        return r

    class Meta:
        model = am.Asset
        fields = ['id', 'url', 'name', 'category', 'parent', 'department',
                  'serial_number', 'make', 'model', 'install_date', 'parts',
                  'properties', 'image_url']
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
