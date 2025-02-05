from django.shortcuts import render
from django.views.generic import ListView, CreateView, DeleteView, DetailView, UpdateView
from django.urls import reverse_lazy

from . import models
from .froms import CreateServiseForm, CreateClientForm


class ServiceCreateView(CreateView):
    model = models.Services
    form_class = CreateServiseForm
    template_name = 'services/service_create.html'
    success_url = 'services'


class ServiceListView(ListView):
    model = models.Services
    template_name = 'services/service_list.html'
    context_object_name = 'services'


class ClientCreateView(CreateView):
    model = models.Clients
    form_class = CreateClientForm
    template_name = 'clients/client_create.html'
    success_url = 'clients'


class ClientListView(ListView):
    model = models.Clients
    template_name = 'clients/client_list.html'
    context_object_name = 'clients'

class ClientShowView(DetailView):
    model = models.Clients
    template_name = 'clients/client_show.html'
    context_object_name = 'client'

class ClientDeleteView(DeleteView):
    model = models.Clients
    template_name = 'clients/client_delete.html'
    success_url = reverse_lazy('client_list')
    context_object_name = 'client'

class ClientUpdateView(UpdateView):
    model = models.Clients
    form_class = CreateClientForm
    template_name = 'clients/client_update.html'
    success_url = reverse_lazy('client_list')