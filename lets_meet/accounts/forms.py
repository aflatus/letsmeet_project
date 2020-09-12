from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError

class UserLoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)

class UserSignupForm(UserCreationForm):
    password1 = forms.CharField(label='Password', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Password Confirmation', widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

    def unique_email(self):
        email = self.cleaned_data.get('email')
        username = self.cleaned_data.get('username')
        if User.objects.filter(email=email).exclude(username=username):
            raise forms.ValidationError(u'Email addresses must be unique.')
        return email

    def equal_password(self):
        password1 = self.cleaned_data.get('password1')
        password2 = self.cleaned_data.get('password2')

        if password1 != password2:
            raise ValidationError("Passwords do not match")

        return password2

