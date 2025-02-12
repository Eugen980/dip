from django.contrib import admin
from django.urls import path, include
from django.contrib.auth.views import LogoutView

from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name='main'),
    path('registration/', views.CreateUser.as_view(), name='registration'),
    path('login/', views.LoginManagerView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('bid/', include('diplom.bid.urls')),
    path('reports/', include('diplom.reports.urls')),
    path('charts/', include('diplom.charts.urls')),
    path('orders/', include('diplom.orders.urls')),
    path('services/', include('diplom.services.urls')),
    path('employee', include('diplom.employees.urls')),
    path('clients/', include('diplom.clients.urls')),
]

