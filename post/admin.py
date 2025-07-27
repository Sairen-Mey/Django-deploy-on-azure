from django.contrib import admin
from .models import Post, PostImage


class ImageInLine(admin.TabularInline):
    model = PostImage
    extra = 3
    max_num = 10

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ("id", "author", "content", "created_at")
    inlines = [ImageInLine]

@admin.register(PostImage)
class ImageAdmin(admin.ModelAdmin):
    list_display = ("id", "post", "image")
