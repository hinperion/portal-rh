from django import forms
from django.utils import timezone

from .models import HolidayRequest

class HolidayRequestForm(forms.ModelForm):
    class Meta:
        
        def clean(self):
            cleaned_data = super().clean()
            
            start_date = cleaned_data.get("start_date")
            end_date = cleaned_data.get("end_date")
            
            if start_date and start_date < timezone.localdate():
                raise forms.ValidationError(
                    "Data inicial não pode ser no passado"
                )
            
            if start_date and end_date:
                if end_date < start_date:
                    raise forms.ValidationError(
                        "Data final não pode ser menor que data inicial"
                    )
            return cleaned_data
        
        model = HolidayRequest
        fields = [
            "start_date",
            "end_date",
        ]
        
        widgets = {
            "start_date": forms.DateInput(
                attrs={"type": "date"}
            ),
            "end_date": forms.DateInput(
                attrs={"type": "date"}
            ),
        }