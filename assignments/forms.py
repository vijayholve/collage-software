from django.forms import ModelForm
from students.models import Assignment ,ClassGroup
from datetime import datetime, date
from django import forms
from django.forms import ModelForm ,DateInput 

class ClassgroupForm(ModelForm):
    
    class Meta:
        model=ClassGroup
        fields="__all__"
class AssignmentForm(ModelForm):
    
    class Meta:
        model=Assignment
        fields=['title','description','subject','due_date','classgroup','assigned_by']  
        widgets = {
            'due_date': DateInput(attrs={'type': 'date'}),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)  # Correctly call the parent class's __init__ method
        for field_name, field in self.fields.items():
            field.widget.attrs['placeholder'] = field.label
    def clean(self):
        cleaned_data = super().clean()
        title = cleaned_data.get('title')
        test_date = cleaned_data.get('test_date')

        if test_date and test_date < date.today():
            self.add_error('due_date', 'Test date must be in the future.')

        if not title:
            self.add_error('title', 'Title is required.')

        # if title and 'exam' not in title.lower():
        #     self.add_error('title', 'Title must contain the word "exam".')

        return cleaned_data

    def clean_title(self):
        title = self.cleaned_data.get('title')
        # if not title:
        #     raise forms.ValidationError('Title is required.')
        # if 'exam' or 'test'  not in title.lower():
        #     raise forms.ValidationError('Title must contain the word "exam".')
        return title

    def clean_test_date(self):
        test_date = self.cleaned_data.get('due_date')
        if test_date:
            # Convert test_date to a datetime.date object if it is a datetime.datetime object
            if isinstance(test_date, datetime):
                test_date = test_date.date()
            if test_date < date.today():
                raise forms.ValidationError('Test date must be in the future.')
        return test_date 
