from dataclasses import field
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.db import transaction
from django.contrib.auth import authenticate, login, logout

from .models import *

class AdminSignUpForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = User
        fields = ["last_name", "first_name", "email", "username"]

    def save(self, commit=True):
        user = super().save(commit=False)
        user.is_admin = True
        if commit:
            user.save()
        return user

class StaffSignUpForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = User
        fields = ["last_name", "first_name", "email", "username"]

    def save(self, commit=True):
        user = super().save(commit=False)
        user.is_staff = True
        if commit:
            user.save()
        return user


class UpdateForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ["last_name", "first_name", "email", "username"]


class UpdatePasswordForm(forms.ModelForm):
    password = forms.CharField(max_length=255, widget=forms.PasswordInput(attrs={'class': 'password-field'}), label="Old Password")
    new_password = forms.CharField(max_length=255, widget=forms.PasswordInput(attrs={'class': 'password-field'}))
    confirm_password = forms.CharField(max_length=255, widget=forms.PasswordInput(attrs={'class': 'password-field'}))
    class Meta:
        model = User
        fields = ["password", "new_password", "confirm_password"]

class SignInForm(forms.Form):
    username = forms.CharField(label='Username')
    password = forms.CharField(
        label="Password",
        strip=False,
        widget=forms.PasswordInput(attrs={"autocomplete": "new-password", "class" : "form-control"}),
    )
 
    class Meta:
        fields = ['username', 'password']