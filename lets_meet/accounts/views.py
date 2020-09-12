from django.shortcuts import render, redirect
from django.contrib import auth
from django.http import HttpResponse
from django.contrib.auth import authenticate
from django.contrib.auth.forms import UserCreationForm
from .forms import UserLoginForm, UserSignupForm


# Create your views here.

def login(request):

    if request.method == 'POST':
        login_form = UserLoginForm(request.POST)
        if login_form.is_valid():
            u = login_form.cleaned_data['username']
            p = login_form.cleaned_data['password']
            user = authenticate(username=u, password=p)

        if user is not None:
            auth.login(request, user)
            return redirect('')
        else:
            login_form.add_error(None, 'Cant sign up now, ')

    else:
        login_form = UserLoginForm()

    return render(request, 'accounts/login.html', {'form': login_form})


def signup(request):

    if request.method == 'POST':
        signup_form = UserSignupForm(request.POST)
        if signup_form.is_valid():

            u = signup_form.cleaned_data['username']
            p = signup_form.cleaned_data['password1']
            user = authenticate(username=u, password=p)

        if user is not None:
            auth.login(request, user)
            return redirect('login')
        else:
            signup_form.add_error(None, 'Username and/or password is incorrect.')

    else:
        signup_form = UserLoginForm()

    return render(request, 'accounts/signup.html', {'form': signup_form})


def logout(request):
    auth.logout(request)
    return redirect('/')


def profile(request):
    return render(request, 'accounts/profile.html')