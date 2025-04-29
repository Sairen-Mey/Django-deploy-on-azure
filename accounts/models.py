# Create your models here.
from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from .managers import CustomUserManager


class User(AbstractBaseUser, PermissionsMixin):
    username = models.CharField(max_length=200, unique=True, blank=False)
    full_name = models.CharField(max_length=200, blank=False)
    email = models.EmailField(null=True)
    avatar = models.ImageField(upload_to="avatars/", default="avatars/baseavatar.jpg")
    bio = models.CharField(max_length=200, blank=True)
    phone_number = models.CharField(max_length=100, blank=False)
    gender = models.CharField(max_length=7)
    date_update = models.DateTimeField(auto_now=True)
    country = models.CharField(max_length=30, blank=False)

    is_staff = models.BooleanField(default=False)

    objects = CustomUserManager()


    USERNAME_FIELD = "username"
    REQUIRED_FIELDS = ["email", "phone"]

    groups = models.ManyToManyField(
        'auth.Group',
        related_name='user_insta',
        blank=True,
    )
    user_permissions = models.ManyToManyField(
        'auth.Permission',
        related_name='user_insta',
        blank=True,
    )
