from django.shortcuts import render,redirect
from students.models import ClassGroup,Classes,Student
from django.db.models.mes
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
        return redirect('home-assignemts', class_id=classgroup.id) 
    else:
        error(request,"Select the Value")
    content = {"classes": classes, "years": years}
    return render(request, "assignements/assignements_classes_list.html", content) 
