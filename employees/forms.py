from django import forms
from django.contrib.auth.models import User

from .models import Employee    

class EmployeeForm(forms.ModelForm):
    first_name = forms.CharField(max_length=150)
    last_name = forms.CharField(max_length=150)
    email = forms.EmailField()
    temporary_password = forms.CharField(
        label="Temporary Password",
        widget=forms.PasswordInput
    )
    
    class Meta:
        model = Employee
        fields = [
            "first_name",
            "last_name",
            "email",
            "cpf",
            "phone",
            "address",
        ]