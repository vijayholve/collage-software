from django.forms import ModelForm 
from students.models import Timetable,TimetableSlot


class timetableform(ModelForm):
    class Meta:
        model=Timetable
        fi