from .models import Profile
from django import forms


class EditProfileForm(forms.ModelForm):

    email = forms.EmailField(required=False)
    username = forms.CharField(required=False, max_length=130)
    class Meta:
        model = Profile
        fields = ["avatar", "bio", "gender", "country"]

    def __init__(self, *args, **kwargs):
        user = kwargs.pop('user')
        super().__init__(*args, **kwargs)


        self.fields['username'].initial = user.username
        self.fields['email'].initial = user.email

        for field in self.fields.values():
            field.required = False

    def save(self, commit=True):
        profile = super().save(commit=False)
        user = profile.user

        username = self.cleaned_data.get('username')
        email = self.cleaned_data.get('email')
        if username:
            user.username = username
        if email:
            user.email = email

        if commit:
            user.save()
            profile.save()
        return profile