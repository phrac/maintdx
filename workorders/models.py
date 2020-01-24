from django.db import models
from django.contrib.auth.models import User
from maintdx.assets.models import Asset
from maintdx.parts.models import Part

class WorkOrderType(models.Model):
    name = models.CharField(max_length=32)
    short_name = models.CharField(max_length=4)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

class WorkOrder(models.Model):
    asset = models.ForeignKey(Asset, related_name='work_orders', on_delete=models.CASCADE)
    wo_type = models.ForeignKey(WorkOrderType, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE)
    closed = models.BooleanField(default=False)
    closed_at = models.DateTimeField(null=True, blank=True)
    due_date = models.DateField(null=True)
    description = models.CharField(max_length=256, blank=True, null=True)
    work_instructions = models.TextField(null=True, blank=True)
    tech_notes = models.TextField(null=True, blank=True)
   
    def __str__(self):
        return self.name

class WorkOrderClock(models.Model):
    work_order = models.ForeignKey(WorkOrder, on_delete=models.CASCADE)
    clock_in = models.DateTimeField(auto_now_add=True)
    clock_out = models.DateTimeField(null=True, blank=True)
    duration = models.DurationField(null=True, blank=True)
    cost = models.DecimalField(max_digits=5, decimal_places=2)
    technician = models.ForeignKey(User, on_delete=models.CASCADE)

    def save(self, *args, **kwargs):
        self.duration = self.clock_out - self.clock_in
        self.cost = self.technician.employee.salary * self.duration
        super(WorkOrderClock, self).save(*arg, **kwargs)

class WorkOrderPart(models.Model):
    work_order = models.ForeignKey(WorkOrder, on_delete=models.CASCADE)
    part = models.ForeignKey(Part, on_delete=models.CASCADE)
    quantity = models.IntegerField(default=0)

    def save(self, *args, **kwargs):
        part.consume_part(self.quantity)
