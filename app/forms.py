from django import forms
from django.forms import ModelForm

from app.models import Car, User


class CarForm(ModelForm):
    class Meta:
        model = Car
        fields = ['model', 'brand', 'year']


class UserForm(ModelForm):
    class Meta:
        model = User
        widgets = {
            'first_name': forms.TextInput(),
            'last_name': forms.TextInput(),
            'email': forms.EmailInput(attrs={'placeholder': 'email@example.com'}),
            'password': forms.PasswordInput()
        }
        fields = ['first_name', 'last_name', 'username', 'email', 'password']

    class LoginForm(ModelForm):
        class Meta:
            model = User
            widgets = {
                'email': forms.EmailInput(attrs={'placeholder': 'email@example.com'}),
                'password': forms.PasswordInput(),
            }
            fields = ['email', 'password']


class UpdateUserForm(ModelForm):
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'email']
