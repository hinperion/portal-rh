from django.contrib.auth import get_user_model
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404

from .models import Employee
from .forms import EmployeeForm

from accounts.decorators import hr_required

User = get_user_model()

@login_required
@hr_required
def employee_list(request):
    employees = Employee.objects.filter(is_active=True)
    
    context = {
        "employees": employees
    }
    return render(request, "employees/employee_list.html", context)

@login_required
@hr_required
def employee_create(request):
    
    if request.method == "POST":
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
        form=EmployeeForm()
        
    return render(
        request,
        "employees/employee_form.html",
        {"form": form}    
    )

@login_required
@hr_required
def employee_update(request, pk):
    
    employee = get_object_or_404(Employee, pk=pk)
    
    if request.method == "POST":
        
        form = EmployeeForm(
            request.POST,
            instance=employee
        )
        
        if form.is_valid():
            
            user = employee.user
            
            user.first_name = form.cleaned_data["first_name"]
            user.last_name = form.cleaned_data["last_name"]
            user.email = form.cleaned_data["email"]
            user.username = form.cleaned_data["email"]
            
            user.save()
            
            form.save()
            
            return redirect("employee_list")
    
        else:
            print(form.erros)
            
    else:
        
        form = EmployeeForm(
            instance=employee,
            initial={
                "first_name": employee.user.first_name,
                "last_name": employee.user.last_name,
                "email": employee.user.email,
            }
        )
    
    return render(
        request,
        "employees/employee_form.html",
        {"form": form}
    )
        
@login_required
@hr_required
def employee_disable(request, pk):
    employee = get_object_or_404(Employee, pk=pk)
    
    employee.is_active = False
    employee.save()
    
    return redirect("employee_list")
    
    
   