from django.contrib import admin
import maintdx.workorders.models as wo

admin.site.register(wo.WorkOrder)
admin.site.register(wo.WorkOrderType)
admin.site.register(wo.WorkOrderPart)
admin.site.register(wo.WorkOrderClock)
