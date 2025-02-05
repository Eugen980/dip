from django.contrib import admin
from django.urls import path

from . import views as v
from .manager import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', v.index, name='main'),
    path('services', views.ServiceListView.as_view(), name='services_list'),
    path('create_service', views.ServiceCreateView.as_view(), name='service_create'),
    path('create_client', views.ClientCreateView.as_view(), name='client_create'),
    path('clients', views.ClientListView.as_view(), name='client_list'),
    path('clients/<int:pk>', views.ClientShowView.as_view(), name='client_show'),
    path('clients/<int:pk>/delete', views.ClientDeleteView.as_view(), name='client_delete'),
    path('clients/<int:pk>/update', views.ClientUpdateView.as_view(), name='client_update'),
]

