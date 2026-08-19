from django.contrib import admin

from .models import HolidayRequest

@admin.register(HolidayRequest)
class HolidayRequestAdmin(admin.ModelAdmin):
    
    list_display = (
        "employee",
        "start_date",
        "end_date",
        "total_days",
        "status",
        "created_at",
       
     )