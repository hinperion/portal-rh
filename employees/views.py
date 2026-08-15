from django.contrib.auth.decorators import login_required
from .models import Employee
from django.shortcuts import render
from .forms import EmployeeForm
from django.contrib.auth.models import User

from accounts.decorators import hr_required

@login_required
@hr_required
def employee_list(request):
    employees = Employee.objects.all()
    
    context = {
        "employees": employees
    }
    return render(request, "employees/employee_list.html", context)

@login_required
@hr_required
def employee_create(request):
    if request.method == "POST":
     form = EmployeeForm(request.POST)
    else:
        form = EmployeeForm()
        
    return render(
        request,
        "employees/employee_form.html",
        {"form": form}
    )
     

