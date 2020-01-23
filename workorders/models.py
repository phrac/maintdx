from django.db import models
from maintdx.assets.models import Asset

class WorkOrderType(models.Model):
    name = models.CharField(max_length=32)
    short_name = models.CharField(max_length=4)
   
    def __str__(self):
        return self.name

class WorkOrder(models.Model):
    asset = models.ForeignKey(Asset, related_name='work_orders', on_delete=models.CASCADE)
    wo_type = models.ForeignKey(WorkOrderType, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    closed = models.BooleanField(default=False)
    due_date = models.DateField(null=True)
    description = models.CharField(max_length=256, blank=True, null=True)
    work_instructions = models.TextField(null=True)
   

    def __str__(self):
        return self.name
