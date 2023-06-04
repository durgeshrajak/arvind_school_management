from django import forms
from .models import SchoolData

class SchoolForm(forms.ModelForm):
    class Meta:
        model = SchoolData
        fields = ['name', 'payable_amount', 'paid_amount', 'date']
        widgets = {
            'name': forms.TextInput(attrs={}),
            'payable_amount': forms.NumberInput(attrs={}),
            'paid_amount': forms.NumberInput(attrs={'style': 'font-weight: bold;'}),
            'date': forms.DateTimeInput(attrs={}),
        }
	
