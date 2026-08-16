from django.urls import path
from .views import employee_list, employee_create, employee_update, employee_disable



urlpatterns = [
    path("", employee_list, name="employee_list"),
    path("new/", employee_create, name="employee_create"),
    path("<int:pk>/edit/", employee_update, name="employee_update"),
    path("<int:pk>/disable/", employee_disable, name="employee_disable"),
    ]