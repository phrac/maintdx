from maintdx.workorders.models import WorkOrder, WorkOrderType
from rest_framework import serializers


class WorkOrderSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = WorkOrder
        fields = [
            "asset",
            "wo_type",
            "created_at",
            "created_by",
            "closed",
            "due_date",
            "description",
        ]
        depth = 1


class WorkOrderTypeSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = WorkOrderType
        fields = ["name", "short_name"]
