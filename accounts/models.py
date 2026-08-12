from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    class Role(models.TextChoices):
        EMPLOYEE = "EMPLOYEE", "Employee"
        HR = "HR", "HR"
        CEO = "CEO", "CEO"
        
    role = models.CharField(
        max_length=20,
        choices=Role.choices,
        default=Role.EMPLOYEE,  
    )
    
    def __str__(self):
        return self.username