from django.db import models
from maintdx.assets.models import Asset

class WorkOrderType(models.Model):
    name = models.CharField(max_length=32)
    short_name = models.CharField(max_length=4)
   
    def __str__(self):
        return self.name

class WorkOrder(models.Model):
    asset = models.ForeignKey(Asset, on_delete=models.CASCADE)
    wo_type = models.ForeignKey(WorkOrderType, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    due_date = models.DateField()
    work_instructions = models.TextField()


    def __str__(self):
        return self.name
