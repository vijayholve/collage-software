from django.shortcuts import render,redirect ,get_object_or_404
from students.models import Timetable ,ClassGroup,Classes ,TimeSlot
from .form import TimetableForm ,timeslotform

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

# templatetags/custom_filters.py
from django import template

register = template.Library()

@register.filter
def get_item(dictionary, key):
    return dictionary.get(key, '')
def create_timeslot_of_timetablel(request):
    form=timeslotform()
    if request.method == "POST":
        form=timeslotform(request.POST)
        if form.is_valid():
            forms=form.save() 
            return redirect('timetable_list',classid=2)
    content={"form":form}
    return render(request,"timetables/create_timetables.html",content)

def create_timetable_of_class(request,classid):
    classgroup=ClassGroup.objects.get(id=classid)
    form=TimetableForm()
    if request.method == "POST":
        form=TimetableForm(request.POST)
        if form.is_valid():
            forms=form.save(commit=True)
            form.classgroup=classgroup
            forms.save()
            return redirect('timetable_list',classid=classid)
    content={"form":form}
    return render(request,"timetables/create_timetables.html",content)

def all_classes(request):
    classes = Classes.objects.all()
    class_ba=Classes.objects.get(name="BA")    
    years = ClassGroup.objects.filter(name=class_ba)
    class_id = request.GET.get('class')
    year_id = request.GET.get('year')

    if request.method ==  "GET" and class_id and year_id:
        class_obj=Classes.objects.get(id=class_id)
        classgroup=ClassGroup.objects.get(name=class_obj,year=year_id)
        return redirect("timetable_list", classid=classgroup.id) 
    # else:
    #     error(request,"Select the Value")
    content = {"classes": classes, "years": years}
    return render(request, "assignements/assignements_classes_list.html", content) 
# views.py


# views.py

from django.shortcuts import render, get_object_or_404
# from .models import ClassGroup, Timetable

# def class_timetable(request, classgroup_id):
#     classgroup = get_object_or_404(ClassGroup, id=classgroup_id)
#     timetable_entries = Timetable.objects.filter(classgroup=classgroup).order_by('day_of_week', 'start_time')

#     # Prepare unique time slots
#     time_slots = timetable_entries.values('start_time', 'end_time').distinct()

#     # Structure data for the template
#     timetable_dict = {}
#     for entry in timetable_entries:
#         key = (entry.start_time, entry.end_time)
#         if key not in timetable_dict:
#             timetable_dict[key] = {}
#         timetable_dict[key][entry.day_of_week] = entry

#     days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"]
#     context = {
#         'classgroup': classgroup,
#         'timetable_dict': timetable_dict,
#         'time_slots': time_slots,
#         'days': days
#     }
#     return render(request, 'timetables/class_timetable.html', context)
# from django.shortcuts import render
# from .models import Timetable, TimeSlot

def timetable_list(request, classid):
    # Fetch all timetables for the given classgroup_id
    classgroup=ClassGroup.objects.get(id=classid)
    timetables = Timetable.objects.filter(classgroup__id=classid)
    
    # Initialize the timetable dictionary
    days_of_week = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday']
    time_slots = TimeSlot.objects.all()
    timetable = {day: {slot: [] for slot in time_slots} for day in days_of_week}
    # Populate the timetable dictionary
    for entry in timetables:
        timetable[entry.day_of_week][entry.time_slot].append(entry)
    
    context = {
        'days_of_week': days_of_week,
        'time_slots': time_slots,
        'timetable': timetable,
        'classgroup': classgroup,
    }
    
    return render(request, 'timetables/timetable_list.html', context)
