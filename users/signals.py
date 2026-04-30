from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import CustomUser
from clients.models import Client

@receiver(post_save, sender=CustomUser)
def create_client_profile(sender, instance, created, **kwargs):
    if created and not instance.is_staff:
        Client.objects.create(
            user=instance,
            first_name=instance.first_name,
            last_name=instance.last_name,
            email=instance.email,
            phone=instance.phone_number or '',
            address=instance.address or ''
        )

@receiver(post_save, sender=CustomUser)
def save_client_profile(sender, instance, **kwargs):
    if hasattr(instance, 'client_profile'):
        instance.client_profile.save()
