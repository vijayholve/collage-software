from django.shortcuts import render,redirect ,get_object_or_404
from students.models import Timetable ,ClassGroup,Classes 
from .form import timetableform 


from django import template

register = template.Library()
@register.filter
def get_slot(timetable_entries, start_time, end_time, day):
    for entry in timetable_entries:
        if (entry.start_time == start_time and 
            entry.end_time == end_time and 
            entry.day_of_week == day):
            return entry
    return None
def create_timetable_of_class(request,class_id):
    form=timetableform()
    if request.method == "POST":
        form=timetableform(request.POST)
        if form.is_valid():
            form.save()
            return redirect('all-classes')
    content={"form":form}
    return render(request,"timetables/create_timetables.html",content)
def timetable_of_class(request,classid):
    pass

def all_classes(request):
    classes = Classes.objects.all()
    class_ba=Classes.objects.get(name="BA")    
    years = ClassGroup.objects.filter(name=class_ba)
    class_id = request.GET.get('class')
    year_id = request.GET.get('year')

    if request.method ==  "GET" and class_id and year_id:
        class_obj=Classes.objects.get(id=class_id)
        classgroup=ClassGroup.objects.get(name=class_obj,year=year_id)
        return redirect("class-timetable", classgroup_id=classgroup.id) 
    # else:
    #     error(request,"Select the Value")
    content = {"classes": classes, "years": years}
    return render(request, "assignements/assignements_classes_list.html", content) 
# templatetags/custom_tags.py
from django import template
from your_app.models import Timetable  # Adjust import based on your actual model

register = template.Library()

@register.simple_tag
def get_slot(timetable_entries, start_time, end_time, day):
    for entry in timetable_entries:
        if (entry.start_time == start_time and 
            entry.end_time == end_time and 
            entry.day_of_week == day):
            return entry
    return None
