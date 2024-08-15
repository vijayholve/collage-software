from django.shortcuts import render ,redirect
from django.contrib.auth.models import User
from django.contrib.auth import login ,authenticate,logout
from  django.contrib import messages
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.db.models import Q
from django.template.defaulttags import register 
from .forms import studuntform ,subjectform  ,CustomUserCreationForm ,TeacherForm,AdminForm
from django.db.models import Q  
from students.models import CustomUser ,Teacher,Student,Subject,hod  ,Test,TestResult
from django.contrib.messages import error

def login_page(request):
    page="login"
    username=request.POST.get("username")
    password=request.POST.get("password")
    if request.method == "POST":
        try:
            user=User.objects.get(username=username)
        except Exception as e:
            messages.error(request,f"error is {e}")
        user=authenticate(request,username=username,password=password)

        if user is not None:
            login(request,user)
            return redirect("home")
        else :
            messages.error(request,"incorect username and password ")
    context={"page":page}
    return render(request,"base/login_page.html",context)
# def register(request):
#     page="resister"
#     if request.method =="POST":
#         return _extracted_from_register_4(request)
#     context={"page":page}
#     return render(request,"base/login_page.html",context)
# TODO Rename this here and in `register`
def _extracted_from_register_4(request):
    fullname=request.POST.get("fullname")
    email=request.POST.get("email")
    username=request.POST.get("username")
    password=request.POST.get("password")
    confirm_password=request.POST.get("confirm-password")
    print(fullname," ",email," ",username," ",password," ",confirm_password)
    if password != confirm_password :
        messages.error(request,"Password Does Not Matching")
        return redirect("register")
    if username is None or len(username) <  3 :
        messages.error(request,"please enter username")
        return redirect("register")
    if fullname is None or len(fullname) <= 5:
        messages.error(request,"please enter fullname")
        return redirect("register")
    if email is None or len(email) <= 5:
        messages.error(request,"please enter email")
        return redirect("register")
    try:
        user = User.objects.create_user(username=username, email=email, password=password)
        user.save()
        if picture:=request.FILES.get("profilePicture"):
            print("Pictrure issaved")
        else:
            picture="images/default.avif"
        # profile = UserProfile.objects.create(user=user, profilePicture=picture, dateOfBirth=None)
        # profile.save()
        login(request, user)
        # send_mail_task.delay(email, fullname)
        return redirect("home")
    except Exception as e:
        print(e)
        messages.error(request, f"error is {e}")
        context = {"page": "register"}
        return render(request, "base/login_page.html", context)

# @login_required(login_url="login-page")
def logout_page(request):
    # user=User.objects.get(id=pk)
    logout(request)
    return redirect("login-page")





def customize_login_page(request):
    username=request.POST.get('username') 
    password=request.POST.get('password')
    if request.method == "POST":
        if customeuser:=authenticate(request, username=username ,password=password ):
            login(request,customeuser) 
            return redirect('home') 
        else :
            messages.error(request,'envalid username or password') 
    content={}
    return render(request,'base/login_page.html')
def customeze_register_page(request): 
    ser_form = CustomUserCreationForm()
    if request.method == "POST": 
        user_form = CustomUserCreationForm(request.POST)
        if user_form.is_valid(): 
            return _extracted_from_register_page_6(user_form, request)
    else: 
        user_form = CustomUserCreationForm() 
    context= {
        'user_form': user_form,
     
    }
    return render(request, 'base/register.html',context)


# TODO Rename this here and in `register_page`
def _extracted_from_register_page_6(user_form, request):
    user = user_form.save()
    user_type = request.POST.get('user_type') 
    print("user type is",user_type)
    authenticate( user)
    login(request,user)
    return redirect('user-type',user_id=user.id ,user_type=user_type)  


def user_panel(request,user_id ,user_type):
    customeuser=CustomUser.objects.get(id=user_id)
    student_form = studuntform()
    teacher_form = TeacherForm() 
    admin_form = AdminForm() 
    print(user_type ," and ",user_id)
    if user_type == 'student':
        student_form = studuntform() 
        if request.method == "POST":
            # student_form = studuntform(request.POST,request.FILES) 
            rollno=request.POST.get('roll_no')
            classgroup=request.POST.get('classgroup')
            classgroup=request.POST.get('profile')
            try:
                std=Student.objects.get(roll_no=rollno,classgroup=classgroup)
            except:
                error(request,"class Group and roll no does not matching")
                return redirect('user-type',user_id=user_id,user_type=user_type)
            if std:
                std.user=customeuser 
                std.save()
                return redirect('home') 
            else:
                print("Does Not matching student")
                return redirect('user-type',user_id=customeuser.id,user_type="student")
    elif user_type == 'teacher':
        teacher_form = TeacherForm() 
        if request.method == "POST": 
            teacher_form=TeacherForm(request.POST) 
            if teacher_form.is_valid(): 
                return _extracted_from_user_panel_12(teacher_form, customeuser) 
            else:
                return redirect('register') 
    elif user_type == 'admin':
        admin_form = AdminForm()
        if request.method == "POST": 
            admin_form = AdminForm(request.POST)
            if admin_form.is_valid(): 
                return _extracted_from_user_panel_12(admin_form, customeuser)
    else:
        # When the request method is GET, ensure all forms are passed
        student_form = studuntform()
        teacher_form = TeacherForm()
        admin_form = AdminForm()

    content={  'student_form': student_form, 
        'teacher_form': teacher_form,
        'admin_form': admin_form,
        'customeuser':customeuser, 
        'user_type':user_type ,
    }
    return render(request,'base/user_type.html',content)


# TODO Rename this here and in `user_panel`
def _extracted_from_user_panel_12(arg0, customeuser):
    student = arg0.save(commit=False) 
     
    student.user = customeuser 
    
    student.save() 
    return redirect('home') 
