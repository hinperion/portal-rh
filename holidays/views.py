from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404
from accounts.decorators import hr_required

from employees.models import Employee
from .forms import HolidayRequestForm
from .models import HolidayRequest

@login_required
def holiday_request_create(request):
    employee = get_object_or_404(
        Employee,
        user=request.user
    )
    
    if request.method == "POST":
        form = HolidayRequestForm(request.POST)

        if form.is_valid():
            holiday_request = form.save(commit=False)
            holiday_request.employee = employee

            if holiday_request.total_days > employee.holiday_balance:
                form.add_error(
                    None,
                    "Você não possui saldo de férias suficiente para esta solicitação."
                )
            else:
                holiday_request.save()
                return redirect("dashboard")

    else:
        form = HolidayRequestForm()

    return render(
        request,
        "holidays/holiday_request_form.html",
        {"form": form}
    )    
    
@login_required
@hr_required
def holiday_request_list(request):
    requests = HolidayRequest.objects.filter(
        status=HolidayRequest.Status.PENDING
    )
    
    return render(
        request,
        "holidays/holiday_request_list.html",
        {"requests": requests}
    )

@login_required
@hr_required
def holiday_request_approve(request, pk):
    holiday_request = get_object_or_404(
        HolidayRequest,
        pk=pk,
        status=HolidayRequest.Status.PENDING
    )
    
    employee = holiday_request.employee
    
    if holiday_request.total_days <= employee.holiday_balance:
        employee.holiday_balance -= holiday_request.total_days
        employee.save()
        
        holiday_request.status = HolidayRequest.Status.APPROVED
        holiday_request.save()
    
    return redirect("holiday_request_list")

@login_required
@hr_required
def holiday_request_reject(request, pk):
    holiday_request = get_object_or_404(
        HolidayRequest,
        pk=pk,
        status=HolidayRequest.Status.PENDING
    )
    
    holiday_request.status = HolidayRequest.Status.REJECTED
    holiday_request.save()
    
    return redirect("holiday_request_list")

@login_required
@hr_required
def holiday_request_history(request):
    requests = HolidayRequest.objects.all().order_by("-created_at")
    
    return render(
        request,
        "holidays/holiday_request_history.html",
        {"requests": requests}
    )