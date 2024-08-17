from django.shortcuts import render,redirect
from students.models import Timetable ,ClassGroup,Classes 
from .form import timetableform 

def create_timetable_of_class(request,class_id):
    form=timetableform()
    if request.method == "POST":
        form=timetableform(request.POST)
        if form.is_valid():
            form.save()
            return redirect('all-classes')
    content={"form":form}
    return render(request,"")
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
        return redirect("class-timetable", class_id=classgroup.id) 
    # else:
    #     error(request,"Select the Value")
    content = {"classes": classes, "years": years}
    return render(request, "assignements/assignements_classes_list.html", content) 

from django.shortcuts import render, get_object_or_404
from .models import ClassGroup, Timetable

def class_timetable(request, classgroup_id):
    classgroup = get_object_or_404(ClassGroup, id=classgroup_id)
    timetable_entries = Timetable.objects.filter(classgroup=classgroup).order_by('day_of_week', 'start_time')

    context = {
        'classgroup': classgroup,
        'timetable_entries': timetable_entries,
    }
    return render(request, 'timetable/class_timetable.html', context)
