from django.db import models
from django.conf import settings
from django.db.models.signals import post_save
from django.dispatch import receiver

# Create your models here.

class Profile(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    avatar = models.ImageField(upload_to="avatars/", default="avatars/baseavatar.jpg")
    bio = models.CharField(max_length=200, blank=True)
    gender = models.CharField(max_length=7)
    country = models.CharField(max_length=30, blank=False)
    updated = models.DateTimeField(auto_now=True)
    created =models.DateTimeField(auto_now_add=True)

    @receiver(post_save, sender=settings.AUTH_USER_MODEL)
    def create_or_update_user_profile(instance, **kwargs):
        """
        Automatically create or update user profile after user save.
        """
        Profile.objects.update_or_create(user=instance, defaults={})

    def __str__(self):
        return f"{self.user.username}'s profile"
