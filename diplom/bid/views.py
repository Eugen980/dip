from django.views.generic import ListView, CreateView, DeleteView, DetailView, UpdateView
from django.urls import reverse_lazy

from . import models
from .forms import CreateBidForm


class BidCreateView(CreateView):
    form_class = CreateBidForm
    template_name = 'bid/bid_create.html'
    success_url = reverse_lazy('bid_list')


class BidListView(ListView):
    model = models.Bid
    template_name = 'bid/bid_list.html'
    context_object_name = 'bid'


class BidShowView(DetailView):
    model = models.Bid
    template_name = 'bid/bid_show.html'
    context_object_name = 'bid'

class BidDeleteView(DeleteView):
    model = models.Bid
    template_name = 'bid/bid_delete.html'
    success_url = reverse_lazy('bid_list')
    context_object_name = 'bid'

class BidUpdateView(UpdateView):
    model = models.Bid
    form_class = CreateBidForm
    template_name = 'bid/bid_update.html'
    success_url = reverse_lazy('bid_list')