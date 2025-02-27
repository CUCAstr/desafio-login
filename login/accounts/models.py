from django.db import models
from django.db.models.signals import pre_save
from django.dispatch import receiver
from django.contrib.auth.models import User

# Create your models here.

@receiver(pre_save, sender=User)
def set_username(sender, instance, **kwargs):
    if not instance.username:
        instance.username = instance.email
