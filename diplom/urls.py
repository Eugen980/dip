from django.contrib import admin
from django.urls import path, include
from django.contrib.auth.views import LogoutView

from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name='main'),
    path('login/', views.LoginManagerView.as_view(), name='login'),
    path('logout/', views.LogoutView.as_view(), name='logout'),
    path('bid/', include('diplom.bid.urls')),
    path('charts/', include('diplom.charts.urls')),
    path('orders/', include('diplom.orders.urls')),
    path('services/', include('diplom.services.urls')),
    path('employee', include('diplom.employees.urls')),
    path('clients/', include('diplom.clients.urls')),
]

