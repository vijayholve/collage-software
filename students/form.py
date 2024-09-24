from django.forms import ModelForm
from students.models import Holiday
from datetime import datetime, date
from django import forms

class holidays_form(ModelForm):
    class Meta:
        model=Holiday
        fields=['name','date','description']
        widgets = {
            'date':forms.DateInput(attrs={'type': 'date'}),
            
        }
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)  # Correctly call the parent class's __init__ method
        for field_name, field in self.fields.items():
            field.widget.attrs['placeholder'] = field.label
    def clean(self):
        cleaned_data = super().clean()
        title = cleaned_data.get('name')
        h_date = cleaned_data.get('date')
        

        # Check if test date is in the future
        if h_date < date.today():
            self.add_error('date', 'date must be in the future.')

        # Required field validation
        if not title:
            self.add_error('name', 'name is required.')