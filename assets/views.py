from django.shortcuts import render
from maintdx.assets import models as am
from rest_framework import viewsets
from maintdx.assets.serializers import AssetSerializer, CategoryPropertySerializer, CategorySerializer, LocationSerializer, DepartmentSerializer
from django_filters import rest_framework as filters

class AssetViewSet(viewsets.ModelViewSet):
    queryset = am.Asset.objects.all().order_by('name')
    serializer_class = AssetSerializer
    filterset_fields = ('make', 'model', 'serial_number', 'department', 'parent')

class CategoryPropertyViewSet(viewsets.ModelViewSet):
    queryset = am.CategoryProperty.objects.all().order_by('key_name')
    serializer_class = CategoryPropertySerializer

class CategoryViewSet(viewsets.ModelViewSet):
    queryset = am.Category.objects.all().order_by('name')
    serializer_class = CategorySerializer

class LocationViewSet(viewsets.ModelViewSet):
    queryset = am.Location.objects.all().order_by('name')
    serializer_class = DepartmentSerializer

class DepartmentViewSet(viewsets.ModelViewSet):
    queryset = am.Department.objects.all().order_by('name')
    serializer_class = DepartmentSerializer
