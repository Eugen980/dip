from django.urls import path

from . import views

urlpatterns = [
    path('', views.ReportListView.as_view(), name='report_list'),
    path('create', views.ReportCreateView.as_view(), name='report_create'),
    path('<int:pk>/delete', views.ReportDeleteView.as_view(), name='report_delete'),
    path('<int:pk>/update', views.ReportUpdateView.as_view(), name='report_update'),
    path('<int:pk>', views.ReportShowView.as_view(), name='report_show'),
]