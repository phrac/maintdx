from django.shortcuts import render
from rest_framework import viewsets
from maintdx.workorders.models import WorkOrder, WorkOrderType
from maintdx.workorders.serializers import WorkOrderSerializer, WorkOrderTypeSerializer

class WorkOrderViewSet(viewsets.ModelViewSet):
    queryset = WorkOrder.objects.all().order_by('id')
    serializer_class = WorkOrderSerializer

class WorkOrderTypeViewSet(viewsets.ModelViewSet):
    queryset = WorkOrderType.objects.all().order_by('name')
    serializer_class = WorkOrderTypeSerializer
