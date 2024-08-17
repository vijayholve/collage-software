from django.forms import ModelForm ,DateInput,TimeInput
from students.models import Timetable,TimetableSlot


class timetableform(ModelForm):
    class Meta:
        model=Timetable
        fields=['classgroup','subject',
                'teacher',
                'day_of_week','start_time',
                'end_time'
                ]
        widgets = {
            'test_date':DateInput(attrs={'type': 'date'}),
            'start_time': forms.TimeInput(attrs={'type': 'time'}),
            'end_time': forms.TimeInput(attrs={'type': 'time'}),
        }