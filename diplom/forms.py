from django.contrib.auth.forms import AuthenticationForm
from django import forms
from django.contrib.auth import get_user_model


class LoginManagerForm(AuthenticationForm):
    username = forms.CharField(label='Логин')
    password = forms.PasswordInput()

    class Meta:
        model = get_user_model()
        fields = ['username', 'password']