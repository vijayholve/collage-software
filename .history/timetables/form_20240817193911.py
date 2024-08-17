

from django import forms
from students.models import Timetable, Subject, Teacher

class TimetableForm(forms.ModelForm):
    class Meta:
        model = Timetable
        fields = ['classgroup', 'subject', 'teacher', 'day', 'start_time', 'end_time']
        widgets = {
            'classgroup': forms.Select(attrs={'class': 'form-control'}),
            'subject': forms.Select(attrs={'class': 'form-control'}),
            'teacher': forms.Select(attrs={'class': 'form-control'}),
            'day': forms.Select(attrs={'class': 'form-control'}),
            'start_time': forms.TimeInput(attrs={'class': 'form-control', 'type': 'time'}),
            'end_time': forms.TimeInput(attrs={'class': 'form-control', 'type': 'time'}),
        }
