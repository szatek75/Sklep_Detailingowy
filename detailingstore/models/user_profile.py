from django.db import models
from django.contrib.auth.models import User  # lub inną klasę użytkownika, którą używasz
from django.db.models.signals import post_save
from django.dispatch import receiver

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=30, blank=True, null=True)  # Pozostawione jako opcjonalne
    last_name = models.CharField(max_length=30, blank=True, null=True)  # Pozostawione jako opcjonalne
    address = models.CharField(max_length=255, blank=True)

@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        UserProfile.objects.create(user=instance)

@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.userprofile.save()
