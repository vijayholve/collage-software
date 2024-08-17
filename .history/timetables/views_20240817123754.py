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
def timetable_of_class*requets

def all_classes(request):
    classes = Classes.objects.all()
    class_ba=Classes.objects.get(name="BA")    
    years = ClassGroup.objects.filter(name=class_ba)
    class_id = request.GET.get('class')
    year_id = request.GET.get('year')

    if request.method ==  "GET" and class_id and year_id:
        class_obj=Classes.objects.get(id=class_id)
        classgroup=ClassGroup.objects.get(name=class_obj,year=year_id)
        return redirect('home-assignemts', class_id=classgroup.id) 
    # else:
    #     error(request,"Select the Value")
    content = {"classes": classes, "years": years}
    return render(request, "assignements/assignements_classes_list.html", content) 