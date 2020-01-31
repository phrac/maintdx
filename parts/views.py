from django.shortcuts import render
from maintdx.parts import models as parts
from rest_framework import viewsets
from maintdx.parts import serializers
from django_filters import rest_framework as filters

class PartViewSet(viewsets.ModelViewSet):
    queryset = parts.Part.objects.all()
    serializer_class = serializers.PartSerializer


# Create your views here.
