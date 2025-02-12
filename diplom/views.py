from django.shortcuts import render
from django.urls import reverse_lazy
from django.contrib.auth.views import LoginView
from django.contrib.auth import get_user_model
from django.views.generic import CreateView

from .forms import LoginManagerForm, CreateUserForm


def index(request):
    return render(request, 'index.html')


class LoginManagerView(LoginView):
    form_class = LoginManagerForm
    template_name = 'login.html'


class CreateUser(CreateView):
    model = get_user_model()
    form_class = CreateUserForm
    template_name = 'user_register.html'
    success_url = reverse_lazy('main')