from django.urls import path

from . import views

urlpatterns = [
    path('', views.EmployeeListView.as_view(), name='employee_list'),
    path('create', views.EmployeeCreateView.as_view(), name='employee_create'),
    path('<int:pk>/delete', views.EmployeeDeleteView.as_view(), name='employee_delete'),
    path('<int:pk>/update', views.EmployeeUpdateView.as_view(), name='employee_update'),
    path('<int:pk>', views.EmployeeShowView.as_view(), name = 'employee_show'),
]