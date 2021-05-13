import graphene
from graphene_django import DjangoObjectType
from graphene_django.filter import DjangoFilterConnectionField
import django_filters
import maintdx.workorders.models as workorders


class WorkOrderTypeNode(DjangoObjectType):
    class Meta:
        model = workorders.WorkOrderType
        filter_fields = {
            "id": ["exact"],
            "name": ["exact", "icontains", "istartswith"],
            "short_name": ["exact", "icontains", "istartswith"],
        }
        interfaces = (graphene.relay.Node,)


class WorkOrderNode(DjangoObjectType):
    class Meta:
        model = workorders.WorkOrder
        filter_fields = {
            "wo_id": ["exact"],
            "asset__id": ["exact"],
            "wo_type__id": ["exact"],
            "closed": ["exact"],
            "due_date": ["exact", "gt", "lt", "gte", "lte"],
        }
        interfaces = (graphene.relay.Node,)


class WorkOrderClockNode(DjangoObjectType):
    class Meta:
        model = workorders.WorkOrderClock
        filter_fields = {"work_order__id": ["exact"], "technician__id": ["exact"]}
        interfaces = (graphene.relay.Node,)


class WorkOrderPartNode(DjangoObjectType):
    class Meta:
        model = workorders.WorkOrderPart
        filter_fields = {"work_order__id": ["exact"], "part__id": ["exact"]}
        interfaces = (graphene.relay.Node,)


class Query(graphene.ObjectType):
    all_work_order_types = DjangoFilterConnectionField(WorkOrderTypeNode)
    all_work_orders = DjangoFilterConnectionField(WorkOrderNode)
    all_work_order_clocks = DjangoFilterConnectionField(WorkOrderClockNode)
    all_work_order_parts = DjangoFilterConnectionField(WorkOrderPartNode)

    work_order_type = graphene.Node.Field(WorkOrderTypeNode)
    work_order = graphene.Node.Field(WorkOrderNode)
    work_order_clock = graphene.Node.Field(WorkOrderClockNode)
    work_order_part = graphene.Node.Field(WorkOrderPartNode)
