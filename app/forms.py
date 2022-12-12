from django import forms
from django.forms import ModelForm

from app.models import Car, User


class CarForm(ModelForm):
    class Meta:
        model = Car
        fields = ['modelo', 'marca', 'ano']


class UserForm(ModelForm):
    class Meta:
        model = User
        widgets = {
            'email': forms.EmailInput(),
            'password': forms.PasswordInput(),
        }
        fields = ['username', 'email', 'password']

