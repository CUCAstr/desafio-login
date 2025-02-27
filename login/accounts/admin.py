from django.contrib import admin
from django.contrib.auth.models import User
from django.db.models.signals import pre_save
from django.dispatch import receiver

# Register your models here.
@receiver(pre_save, sender=User)
def set_username(sender, instance, **kwargs):
    if not instance.username:
        instance.username = instance.email
