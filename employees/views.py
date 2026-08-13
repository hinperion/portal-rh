from django.contrib.auth.decorators import login_required
from django.shortcuts import render

from accounts.decorators import hr_required

@login_required
@hr_required
def employee_list(request):
    return render(request, "employees/employee_list.html")

# Create your views here.
