from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.forms import ModelForm

from .models import UserModel


class AddUserForm(ModelForm):
    class Meta:
        model = UserModel
        fields = ['username', 'email', 'password1', 'password2']
