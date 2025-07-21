from django.db import models
from django.conf import settings
# Create your models here.

class Subscription(models.Model):
    subscriber = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="following_set")
    target = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="followers_set")
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ('subscriber', 'target')
        ordering = ["-created_at"]

    def __str__(self):
        return f'{self.subscriber.username} following to {self.target.username}'