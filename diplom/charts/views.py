from django.views.generic import ListView, CreateView, DeleteView, DetailView, UpdateView
from django.urls import reverse_lazy

from . import models
from .forms import CreateChartForm


class ChartCreateView(CreateView):
    form_class = CreateChartForm
    template_name = 'charts/chart_create.html'
    success_url = reverse_lazy('chart_list')


class ChartListView(ListView):
    model = models.Charts
    template_name = 'charts/chart_list.html'
    context_object_name = 'chart'


class ChartShowView(DetailView):
    model = models.Charts
    template_name = 'charts/chart_show.html'
    context_object_name = 'chart'

class ChartDeleteView(DeleteView):
    model = models.Charts
    template_name = 'charts/chart_delete.html'
    success_url = reverse_lazy('chart_list')
    context_object_name = 'chart'

class ChartUpdateView(UpdateView):
    model = models.Charts
    form_class = CreateChartForm
    template_name = 'charts/chart_update.html'
    success_url = reverse_lazy('chart_list')
