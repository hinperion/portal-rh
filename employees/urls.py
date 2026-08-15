from django.urls import path
from .views import employee_list, employee_create


urlpatterns = [
    path("", employee_list, name="employee_list"),
    path("new/", employee_create, name="employee_create")
    ]