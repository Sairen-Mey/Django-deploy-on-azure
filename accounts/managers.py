from django.contrib.auth.base_user import BaseUserManager
from .utils import validate_required_fields


class CustomUserManager(BaseUserManager):
    """
    Custom user manager that requires email, username, and full name.
    """

    def create_user(self, username: str, full_name: str, password: str | None = None, **extra_fields):
        """
        Create and return a regular user.
        Expects either email or phone_number in extra_fields.
        """
        validate_required_fields(username=username, full_name=full_name)

        email = extra_fields.get('email')
        phone = extra_fields.get('phone_number')

        if not email and not phone:
            raise ValueError("You must provide at least an email or phone number.")

        if email:
            extra_fields['email'] = self.normalize_email(email)

        user = self.model(
            username=username,
            full_name=full_name,
            **extra_fields
        )
        user.set_password(password)
        user.save()
        return user

    def create_superuser(self, username: str, full_name: str, email:str, password: str | None = None, **extra_fields):
        """
        Create and return a superuser.
        """
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        return self.create_user(username, full_name, password, email=email, **extra_fields)
