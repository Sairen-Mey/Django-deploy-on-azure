from .models import User
from django import forms
from django.core.exceptions import ValidationError
from django.contrib.auth import authenticate, get_user_model
class RegisterForm(forms.ModelForm):
    password = forms.CharField(max_length=65, widget=forms.PasswordInput, label='Input password')
    confirm_password = forms.CharField(max_length=65, widget=forms.PasswordInput, label='Repeat password')
    class Meta():
        model = User
        fields = ['email', 'full_name', 'username']

    def clean(self):
        cleaned_data = super().clean()
        password = cleaned_data.get('password')
        confirm_password = cleaned_data.get('confirm_password')
        if password != confirm_password:
            raise forms.ValidationError("Passwords don't match")
        return cleaned_data

    def save(self, commit=True):
        user = super().save(commit=False)
        user.set_password(self.cleaned_data['password'])
        if commit:
            user.save()
        return user


class LoginForm(forms.Form):
    email = forms.EmailField(label="Email", max_length=255)
    password = forms.CharField(widget=forms.PasswordInput, label="Password", min_length=8)

    def clean(self):
        cleaned = super().clean()
        email = cleaned.get('email')
        pwd = cleaned.get('password')
        User = get_user_model()

        try:
            user = User.objects.get(email=email)
        except User.DoesNotExist:
            raise ValidationError("Невірний email або пароль.")

        if not user.check_password(pwd):
            raise ValidationError("Невірний email або пароль.")

        self.user = user
        return cleaned

