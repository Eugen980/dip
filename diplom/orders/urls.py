from django.urls import path

from . import views

urlpatterns = [
    path('', views.OrderListView.as_view(), name='order_list'),
    path('create', views.OrderCreateView.as_view(), name='order_create'),
    path('<int:pk>/delete', views.OrderDeleteView.as_view(), name='order_delete'),
    path('<int:pk>/update', views.OrderUpdateView.as_view(), name='order_update'),
    path('<int:pk>', views.OrderShowView.as_view(), name='order_show'),
]