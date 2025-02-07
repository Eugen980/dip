from django.views.generic import ListView, CreateView, DeleteView, DetailView, UpdateView
from django.urls import reverse_lazy

from . import models
from .forms import CreateEmployeeForm


class EmployeeCreateView(CreateView):
    form_class = CreateEmployeeForm
    template_name = 'services/service_create.html'
    success_url = reverse_lazy('service_list')


class EmployeeListView(ListView):
    model = models.Emolyees
    template_name = 'services/service_list.html'
    context_object_name = 'services'


class EmployeeShowView(DetailView):
    model = models.Emolyees
    template_name = 'services/service_show.html'
    context_object_name = 'service'

class EmployeeDeleteView(DeleteView):
    model = models.Emolyees
    template_name = 'services/service_delete.html'
    success_url = reverse_lazy('service_list')
    context_object_name = 'service'

class EmployeeUpdateView(UpdateView):
    model = models.Emolyees
    form_class = CreateEmployeeForm
    template_name = 'services/service_update.html'
    success_url = reverse_lazy('service_list')