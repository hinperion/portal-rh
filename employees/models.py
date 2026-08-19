from django.conf import settings
from django.db import models

class Employee(models.Model):
    user = models.OneToOneField(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="employee",  
    )
# Create your models here.
    cpf = models.CharField(max_length=14, unique=True)
    phone = models.CharField(max_length=20)
    address = models.TextField()
    is_active = models.BooleanField(default=True)
    holiday_balance = models.PositiveIntegerField(default=30)
    
    def __str__(self):
        return self.user.get_full_name() or self.user.username
    
