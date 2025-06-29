from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth import get_user_model
from django.contrib.auth.decorators import login_required
from .models import Profile
from .forms import EditProfileForm

User = get_user_model()

def profile_view(request, username):
    user = get_object_or_404(User, username=username)
    profile = get_object_or_404(Profile, user=user)
    return render(request, 'user/profile.html', {'profile':profile})

@login_required
def edit_profile_view(request):
    profile = get_object_or_404(Profile, user=request.user)

    if request.method == "POST":
        form = EditProfileForm(request.POST, request.FILES, instance=profile, user=request.user)
        if form.is_valid():
            form.save()

            return redirect("user:profile", username=form.cleaned_data['username'])
    else:
        form = EditProfileForm(instance=profile, user=request.user)
    return render(request, 'user/edit_profile.html', {"form":form})