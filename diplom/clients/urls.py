from django.urls import path

from . import views


urlpatterns = [
    path('', views.ClientListView.as_view(), name='client_list'),
    path('create', views.ClientCreateView.as_view(), name='client_create'),
    path('<int:pk>', views.ClientShowView.as_view(), name='client_show'),
    path('<int:pk>/delete', views.ClientDeleteView.as_view(), name='client_delete'),
    path('<int:pk>/update', views.ClientUpdateView.as_view(), name='client_update'),
]