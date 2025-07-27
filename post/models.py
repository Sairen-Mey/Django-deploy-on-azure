from django.db import models
from django.conf import settings
from .utils import post_image_upload_path
from PIL import Image
from io import BytesIO
from django.core.files.base import ContentFile
# Create your models here.

class Post(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="posts")
    content = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)
    is_published = models.BooleanField(default=True)

    def __str__(self):
        return f'Post by {self.author.username}'

class Like(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="likes")
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name="likes")
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ('user', 'post')



class Tag(models.Model):
    name = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return f'Post by {self.author.username}'

class PostTag(models.Model):
    post = models.ForeignKey("Post", on_delete=models.CASCADE, related_name="post_tags")
    tag = models.ForeignKey("Tag", on_delete=models.CASCADE, related_name="post_tags")

    def __str__(self):
        return f'Post by {self.author.username}'



class PostImage(models.Model):
    post = models.ForeignKey('Post', on_delete=models.CASCADE, related_name='post_images')
    image = models.ImageField(upload_to='post_images/')



