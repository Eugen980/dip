from django.shortcuts import render
from django.views.generic import ListView, CreateView

from .models import Services
from .froms import CreateServiseForm


class ServiceCreateView(CreateView):
    model = Services
    form_class = CreateServiseForm
    template_name = 'services/service_create.html'
    success_url = 'services'


class ServiceListView(ListView):
    model = Services
    template_name = 'services/service_list.html'
    context_object_name = 'services'
# Create your views here.
