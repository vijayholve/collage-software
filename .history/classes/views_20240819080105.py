from django.shortcuts import render ,redirect   
from .forms import classesform
from students.models import Classes ,ClassGroup
from django.contrib.messages import error
from django.contrib.auth.decorators import login_required

@login_required(login_url="login-page")
def create_classes(request): 
    form=classesform() 
    if request.method == "POST": 
        form=classesform(request.POST,request.FILES) 
        if form.is_valid(): 
            form.save() 
            return redirect('all-classes') 
        else:
            error(request,"Information is incorect")
    content={"form":form    }
    return render(request,"classes/create_class.html", content)
@login_required(login_url="login-page")
def classes_list(request):
    classes=ClassGroup.objects.all()
    content={"classes":classes}
    return render(request,"classes/classes_list.html",content)