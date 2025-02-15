from django.contrib.auth.forms import AuthenticationForm
from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm


class LoginManagerForm(AuthenticationForm):
    username = forms.CharField(label='Логин')
    password = forms.PasswordInput()

    class Meta:
        model = get_user_model()
        fields = ['username', 'password']

class CreateUserForm(UserCreationForm):

    class Meta:
        model = get_user_model()
        fields = ['username']