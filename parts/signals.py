from django.db import models
from django.dispatch import receiver

from maintdx.parts.models import PartInventoryItem, Part

@receiver(models.signals.post_save, sender=PartInventoryItem)
def update_on_hand(sender, instance, **kwargs):
    print('in signal')
    agg = PartInventoryItem.objects.filter(part=instance.part).aggregate(models.Sum('current_on_hand'))
    count = agg['current_on_hand__sum']
    if count is None:
        count = 0
    instance.part.on_hand = count
    instance.part.save()
