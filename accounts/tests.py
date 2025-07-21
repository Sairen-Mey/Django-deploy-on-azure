from django.test import TestCase
from django.contrib.auth import get_user_model
from accounts.forms import RegisterForm, LoginForm

User = get_user_model()

class RegisterFormTests(TestCase):
    def test_valid_with_email(self):
        form = RegisterForm(data={
            "username" : "test1",
            "full_name" : "test2",
            "email" : "2@gmail.com",
            "password" : "1234",
            "confirm_password" : "1234"
        })
        self.assertTrue(form.is_valid())

    def test_empty_email(self):
        form = RegisterForm(data={
            "username" : "test1",
            "full_name" : "test2",
            "email" : "",
            "password" : "1234",
            "confirm_password" : "1234"
        })
        self.assertFalse(form.is_valid())

    def test_passwords_dont_equal(self):
        form = RegisterForm(data={
            "username" : "test1",
            "full_name" : "test2",
            "email" : "",
            "password" : "1234",
            "confirm_password" : "4321"
        })
        self.assertFalse(form.is_valid())
        # self.assertIn("confirm_password", form.errors)
    def test_passwords_are_empty(self):
        form = RegisterForm(data={
            "username" : "test1",
            "full_name" : "test2",
            "email" : "",
            "password" : "",
            "confirm_password" : ""
        })
        self.assertFalse(form.is_valid())
        self.assertIn("password", form.errors)
    def test_empty_username(self):
        form = RegisterForm(data={
            "username" : "",
            "full_name" : "test2",
            "email" : "",
            "password" : "1234",
            "confirm_password" : "1234"
        })
        self.assertFalse(form.is_valid())
    def test_empty_fullname(self):
        form = RegisterForm(data={
            "username" : "test1",
            "full_name" : "",
            "email" : "",
            "password" : "1234",
            "confirm_password" : "1234"
        })
        self.assertFalse(form.is_valid())
        self.assertIn("full_name", form.errors)

    def test_duplicat_username(self):
        User.objects.create_user(username="John", full_name="Carr", email="3@gmail.com", password="1234")

        form = RegisterForm(data={
            "username": "John",
            "full_name": "Carr",
            "email": "6@gmail.com",
            "password": "1234",
            "confirm_password": "1234"
        })
        self.assertFalse(form.is_valid())
        self.assertIn("username", form.errors)

    def test_duplicat_email(self):
        User.objects.create_user(username="John", full_name="Carr", email="3@gmail.com", password="1234")

        form = RegisterForm(data={
            "username": "Nhoj",
            "full_name": "arr",
            "email": "3@gmail.com",
            "password": "1234",
            "confirm_password": "1234"
        })
        self.assertFalse(form.is_valid())
        self.assertIn("email", form.errors)
