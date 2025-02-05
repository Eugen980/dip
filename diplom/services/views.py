from django.views.generic import ListView, CreateView, DeleteView, DetailView, UpdateView
from django.urls import reverse_lazy

from . import models
from .forms import CreateServiseForm


class ServiceCreateView(CreateView):
    form_class = CreateServiseForm
    template_name = 'services/service_create.html'
    success_url = reverse_lazy('service_list')


class ServiceListView(ListView):
    model = models.Services
    template_name = 'services/service_list.html'
    context_object_name = 'services'


class ServiceShowView(DetailView):
    model = models.Services
    template_name = 'services/service_show.html'
    context_object_name = 'service'

class ServiceDeleteView(DeleteView):
    model = models.Services
    template_name = 'services/service_delete.html'
    success_url = reverse_lazy('service_list')
    context_object_name = 'service'

class ServiceUpdateView(UpdateView):
    model = models.Services
    form_class = CreateServiseForm
    template_name = 'services/service_update.html'
    success_url = reverse_lazy('service_list')
