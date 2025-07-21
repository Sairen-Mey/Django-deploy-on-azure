from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import get_user_model
from django.contrib import messages
from django.urls import reverse
from .models import Subscription
# Create your views here.

User = get_user_model()

@login_required
def follow_toggle(request, username):
    target = get_object_or_404(User, username=username)

    if target == request.user:
        messages.error(request,"You cannot subscribe to yourself")
        return redirect(reverse("user:profile", kwargs={"username":username}))

    sub, created = Subscription.objects.get_or_create(subscriber=request.user, target=target)

    if not created:
        sub.delete()
    return redirect(reverse("user:profile", kwargs={"username":username}))

