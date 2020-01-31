from django.shortcuts import render
from maintdx.parts import models as parts
from rest_framework import viewsets
from maintdx.parts import serializers
from django_filters import rest_framework as filters

class PartViewSet(viewsets.ModelViewSet):
    queryset = parts.Part.objects.all()
    serializer_class = serializers.PartSerializer
    filterset_fields = ['part_number']

class PartVendorViewSet(viewsets.ModelViewSet):
    queryset = parts.PartVendor.objects.all()
    serializer_class = serializers.PartVendorSerializer
    filterset_fields = ['part', 'vendor']

class InventoryLocationViewSet(viewsets.ModelViewSet):
    queryset = parts.InventoryLocation.objects.all()
    serializer_class = serializers.InventoryLocationSerializer
    filterset_fields = ['code']

class PartInventoryItemViewSet(viewsets.ModelViewSet):
    queryset = parts.PartInventoryItem.objects.all()
    serializer_class = serializers.PartInventoryItem
    filterset_fields = ['part', 'vendor', 'current_on_hand', 'inventory_location']
