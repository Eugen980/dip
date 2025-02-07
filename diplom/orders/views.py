from django.views.generic import ListView, CreateView, DeleteView, DetailView, UpdateView
from django.urls import reverse_lazy

from . import models
from .forms import CreateOrderForm


class OrderCreateView(CreateView):
    form_class = CreateOrderForm
    template_name = 'orders/order_create.html'
    success_url = reverse_lazy('order_list')


class OrderListView(ListView):
    model = models.Orders
    template_name = 'orders/order_list.html'
    context_object_name = 'order'


class OrderShowView(DetailView):
    model = models.Orders
    template_name = 'orders/order_show.html'
    context_object_name = 'order'

class OrderDeleteView(DeleteView):
    model = models.Orders
    template_name = 'orders/order_delete.html'
    success_url = reverse_lazy('order_list')
    context_object_name = 'order'

class OrderUpdateView(UpdateView):
    model = models.Orders
    form_class = CreateOrderForm
    template_name = 'orders/order_update.html'
    success_url = reverse_lazy('order_list')
