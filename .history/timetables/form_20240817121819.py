from django.forms import ModelForm 
from students.models import Timetable,TimetableSlot


class timetableform(ModelForm):
    class Meta:
        model=Timetable
        fields=['classgroup',
'subject',
'teacher',
day_of_week
start_time
end_time]