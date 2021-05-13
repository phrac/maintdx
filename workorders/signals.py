from django.db import models
from django.dispatch import receiver

from maintdx.workorders.models import WorkOrder, WorkOrderPart


@receiver(models.signals.post_save, sender=WorkOrder)
def update_work_order_parts(sender, instance, **kwargs):
    if instance.closed is True:
        wop = WorkOrderPart.objects.filter(work_order=instance)
        for w in wop:
            if w.processed is False:
                w.consumed_cost = w.part.consume_part(w.quantity)
                w.processed = True
                w.save()
