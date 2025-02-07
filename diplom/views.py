from django.shortcuts import render
from django.contrib.auth.views import LoginView, LogoutView

from .forms import LoginManagerForm


def index(request):
    return render(request, 'index.html')


class LoginManagerView(LoginView):
    form_class = LoginManagerForm
    template_name = 'login.html'
