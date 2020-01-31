from maintdx.parts import models as parts
from django.conf import settings
from rest_framework import serializers

class PartSerializer(serializers.HyperlinkedModelSerializer):
    current_on_hand = serializers.IntegerField(source='get_on_hand_quantity')

    class Meta:
        model = parts.Part
        fields = ['id', 'url', 'part_number', 'description', 'image', 'current_on_hand',
                  'reorder_point', 'max_on_hand'
        ]

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
