from maintdx.workorders.models import WorkOrder, WorkOrderType
from rest_framework import serializers

class WorkOrderSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = WorkOrder
        fields = ['asset', 'wo_type', 'created_at', 'closed', 'due_date',
                  'description']

class WorkOrderTypeSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = WorkOrderType
        fields = ['name', 'short_name']
