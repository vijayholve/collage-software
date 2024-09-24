from django.shortcuts import render,redirect ,get_list_or_404,get_object_or_404
from students.models import ClassGroup,Classes,Student
from django.contrib.messages import error 
from django.contrib.auth.decorators import login_required

# Create your views here.
@login_required(login_url="login-page")
def all_classes(request):
    classes = Classes.objects.all()
    class_ba=Classes.objects.get(name="BA")    
    years = ClassGroup.objects.filter(name=class_ba)
    class_id = request.GET.get('class')
    year_id = request.GET.get('year')

    if request.method ==  "GET" and class_id and year_id:
        class_obj=Classes.objects.get(id=class_id)
        classgroup=ClassGroup.objects.get(name=class_obj,year=year_id)
        return redirect('class-informations', class_id=classgroup.id) 
    else:
        error(request,"Select the Value")
    content = {"classes": classes, "years": years}
    return render(request, "informations/classes_list.html", content) 

def class_information(request,class_id):
    classgroup = get_object_or_404(ClassGroup, id=class_id)
    students = Student.objects.filter(classgroup=classgroup)
    content={"classgroup":classgroup,"students":students}
    return render(request,"informations/class_information.html",content)

def delete_student(request,id,class_id):
    student=Student.objects.get(id=id)
    student.delete()
    return redirect("class-informations",class_id=class_id)