from django.shortcuts import render
from students.models import Timetable ,ClassGroup,Classes 
from .form import timetableform
def timetable_of_class(request,class_id):
    form=timetableform()
    if request.method == ""
