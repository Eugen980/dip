from django.urls import path

from . import views

urlpatterns = [
    path('', views.ChartListView.as_view(), name='chart_list'),
    path('create', views.ChartCreateView.as_view(), name='chart_create'),
    path('<int:pk>/delete', views.ChartDeleteView.as_view(), name='chart_delete'),
    path('<int:pk>/update', views.ChartUpdateView.as_view(), name='chart_update'),
    path('<int:pk>', views.ChartShowView.as_view(), name='chart_show'),
]