from django.views.generic import ListView, CreateView, DeleteView, DetailView, UpdateView
from django.urls import reverse_lazy

from . import models
from .forms import CreateEmployeeForm


class EmployeeCreateView(CreateView):
    form_class = CreateEmployeeForm
    template_name = 'employees/employee_create.html'
    success_url = reverse_lazy('employee_list')


class EmployeeListView(ListView):
    model = models.Emolyees
    template_name = 'employees/employee_list.html'
    context_object_name = 'employee'


class EmployeeShowView(DetailView):
    model = models.Emolyees
    template_name = 'employees/employee_show.html'
    context_object_name = 'employee'

class EmployeeDeleteView(DeleteView):
    model = models.Emolyees
    template_name = 'employees/employee_delete.html'
    success_url = reverse_lazy('employee_list')
    context_object_name = 'employee'

class EmployeeUpdateView(UpdateView):
    model = models.Emolyees
    form_class = CreateEmployeeForm
    template_name = 'employees/employee_update.html'
    success_url = reverse_lazy('employee_list')