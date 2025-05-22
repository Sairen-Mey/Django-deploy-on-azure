from .models import Profile
from django import forms



class EditProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ["avatar", "bio", "gender", "country"]

