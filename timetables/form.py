

from django import forms
from students.models import Timetable, Subject, Teacher ,TimeSlot

class TimetableForm(forms.ModelForm):
    class Meta:
        model = Timetable
        fields = [ 'subject', 'teacher', 'time_slot','day_of_week']    
        widgets = {
            'subject': forms.Select(attrs={'class': 'form-control'}),
            'teacher': forms.Select(attrs={'class': 'form-control'}),
            'day_of_week': forms.Select(attrs={'class': 'form-control'}),

        }

class timeslotform(forms.ModelForm):
    class Meta:
        model=TimeSlot
        fields=[
 'start_time',
'end_time']
        widgets= {
            'start_time': forms.TimeInput(attrs={'class': 'form-control', 'type': 'time'}),
            'end_time': forms.TimeInput(attrs={'class': 'form-control', 'type': 'time'}),
        }