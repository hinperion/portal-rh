from django.contrib.auth import get_user_model
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect

from .models import Employee
from .forms import EmployeeForm

from accounts.decorators import hr_required

User = get_user_model()

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
    
    if request.method =="POST":
        form = EmployeeForm(request.POST)
        
        if form.is_valid():
            email = form.cleaned_data["email"]
            
            user = User.objects.create_user(
                username=email,
                email=email,
                first_name=form.cleaned_data["first_name"],
                last_name=form.cleaned_data["last_name"],
                password=form.cleaned_data["temporary_password"],
            )
            
            employee = form.save(commit=False)
            employee.user = user
            employee.save()
            
            return redirect("employee_list")
        
        else:
            print(form.errors)
            
    else: 
        form = EmployeeForm()
        
    return render(
        request,
        "employees/employee_form.html",
        {"form": form}
    )