from django.shortcuts import render, get_object_or_404
from django.contrib.auth import get_user_model
from .models import Profile


User = get_user_model()

def profile_view(request, username):
    user = get_object_or_404(User, username=username)
    profile = get_object_or_404(Profile, user=user)
    return render(request, 'profile.html', {'profile':profile})
