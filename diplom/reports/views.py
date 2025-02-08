from django.views.generic import ListView, CreateView, DeleteView, DetailView, UpdateView
from django.urls import reverse_lazy

from . import models
from .forms import CreateReportForm


class ReportCreateView(CreateView):
    form_class = CreateReportForm
    template_name = 'reports/report_create.html'
    success_url = reverse_lazy('report_list')


class ReportListView(ListView):
    model = models.Reports
    template_name = 'reports/report_list.html'
    context_object_name = 'report'


class ReportShowView(DetailView):
    model = models.Reports
    template_name = 'reports/report_show.html'
    context_object_name = 'report'

class ReportDeleteView(DeleteView):
    model = models.Reports
    template_name = 'reports/report_delete.html'
    success_url = reverse_lazy('report_list')
    context_object_name = 'report'

class ReportUpdateView(UpdateView):
    model = models.Reports
    form_class = CreateReportForm
    template_name = 'reports/report_update.html'
    success_url = reverse_lazy('report_list')