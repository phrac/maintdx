from maintdx.parts import models as parts
from django.conf import settings
from rest_framework import serializers

class PartSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = parts.Part
        fields = '__all__'

class PartVendorSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = parts.PartVendor
        fields = '__all__'

class InventoryLocationSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = parts.InventoryLocation
        fields = '__all__'

class PartInventoryItem(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = parts.PartInventoryItem
        fields = '__all__'
