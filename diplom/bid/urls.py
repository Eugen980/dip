from django.urls import path

from . import views

urlpatterns = [
    path('', views.BidListView.as_view(), name='bid_list'),
    path('create', views.BidCreateView.as_view(), name='bid_create'),
    path('<int:pk>/delete', views.BidDeleteView.as_view(), name='bid_delete'),
    path('<int:pk>/update', views.BidUpdateView.as_view(), name='bid_update'),
    path('<int:pk>', views.BidShowView.as_view(), name='bid_show'),
]