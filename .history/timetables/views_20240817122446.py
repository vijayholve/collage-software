from django.shortcuts import render,redirect
from students.models import Timetable ,ClassGroup,Classes 
from .form import timetableform
def timetable_of_class(request,class_id):
    form=timetableform()
    if request.method == "POST":
        form=timetableform(request.POST)
        if form.is_valid():
            form.save()
            return redirect('all-classes')
    content={"form":form}
    return render(request)