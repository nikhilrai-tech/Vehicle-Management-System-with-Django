from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import Vehicle

@receiver(post_save, sender=Vehicle)
def delete_vehicle_on_verification(sender, instance, created, **kwargs):
    if instance.verified_by_superuser:
        instance.delete()