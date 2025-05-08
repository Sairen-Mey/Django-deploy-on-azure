from django.shortcuts import render, redirect, get_object_or_404
from django.template import loader, Template
from django.http import HttpResponse
from .forms import RegisterForm, LoginForm
from django.contrib import messages
from django.contrib.auth import login

# Create your views here.


def login_view(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            user = form.user
            login(request, user)
            messages.success(request, 'login is cool')
            return redirect('user:profile')
        else:
            messages.error(request, 'date is wrong')
    else:
        form = LoginForm()
    return render(request, 'login.html', {'form': form})

def registration(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST, request.FILES)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, 'Account create')
            return redirect('user:profile')
        else:
            messages.error(request, 'Edit your request on the form')
    else:
        form = RegisterForm()
    return render(request, 'registration.html', {'form': form})

