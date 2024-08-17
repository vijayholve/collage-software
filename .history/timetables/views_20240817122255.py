from django.shortcuts import render
from students.models import Timetable ,ClassGroup,Classes 

def timetable_of_class(request,class_id):
    form=time
