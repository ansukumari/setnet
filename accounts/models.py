from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.CharField(max_length=500, blank=True)
    dp = models.ImageField(upload_to = lambda instance, filename: '/'.join(['images', 'dp', str(instance.pk)]))
    cp = models.ImageField(upload_to = lambda instance, filename: '/'.join(['images', 'cp', str(instance.pk)]))
    birth_date = models.DateField(null=True, blank=True)

@receiver(post_save, sender=User)
def update_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)
    instance.profile.save()