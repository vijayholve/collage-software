

from django import forms
from students.models import Timetable, Subject, Teacher

class TimetableForm(forms.ModelForm):
    class Meta:
        model = Timetable
        fields = ['classgroup', 'subject', 'teacher', 'time_slot']    
        widgets = {
            'classgroup': forms.Select(attrs={'class': 'form-control'}),
            'subject': forms.Select(attrs={'class': 'form-control'}),
            'teacher': forms.Select(attrs={'class': 'form-control'}),
            
        }

class timeslot(for)