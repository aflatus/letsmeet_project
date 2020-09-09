from django.shortcuts import render, redirect
from django.contrib import auth
from django.http import HttpResponse
from django.contrib.auth import authenticate
from django.contrib.auth.forms import UserCreationForm
from .forms import UserLoginForm, UserRegistrationForm


# Create your views here.

def login(request):
    #TODO login.html
    return render(request, 'accounts/login.html',)


def signup(request):
    #TODO signup.html
    return render(request, 'accounts/signup.html', )


def logout(request):
    auth.logout(request)
    return redirect('/')


def profile(request):
    #TODO profile.html
    return render(request, 'accounts/profile.html')