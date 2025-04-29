from django.urls import path
from django.contrib.auth.views import LogoutView

from . import views

app_name = 'accounts'
urlpatterns = [
    path('registration/', views.registration, name='registration'),
    path('', views.login_view, name='login'),
    path('logout/', LogoutView.as_view(next_page="accounts:login"), name='logout')

]
