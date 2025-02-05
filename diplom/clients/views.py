from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, DeleteView, DetailView, UpdateView

from . import models
from .forms import CreateClientForm

class ClientCreateView(CreateView):
    model = models.Clients
    form_class = CreateClientForm
    template_name = 'clients/client_create.html'
    success_url = reverse_lazy('client_list')


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
