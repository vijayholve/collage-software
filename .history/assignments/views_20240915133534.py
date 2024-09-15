from django.shortcuts import render ,redirect ,get_object_or_404 
from .forms import AssignmentForm 
from django.contrib.messages import error
from students.models import Teacher ,CustomUser ,Assignment  ,ClassGroup ,Classes ,Student ,AssignmentSubmission
from students.models import Assignment
from django.http import FileResponse, Http404 ,HttpResponse 
from .task import send_mail_to_all_students_for_assignemt 
import os 
from datetime import datetime
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
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


    # classes = ClassGroup.objects.filter(name__id=class_id)
    # Add logic to render the class group view


def all_year_list(request ,class_id):
    classes=ClassGroup.objects.filter(name__id=class_id)
    content={"classes":classes} 
    return render(request,"assignements/assignemts_year_list.html",content)
def download_file(request, file_id):
    downloadable_file = get_object_or_404(Assignment, id=file_id)
    file_path = downloadable_file.description.path  
    if os.path.exists(file_path):
        with open(file_path, 'rb') as file:  
            response = HttpResponse(file.read(), content_type='application/octet-stream')
            response['Content-Disposition'] = f'attachment; filename={os.path.basename(file_path)}'
            return response 
    else:
        raise Http404("File not found")
def assignemt_form(request):
    form=AssignmentForm() 
    # teacher=Teacher.objects.get(name="hod2")
    if request.method == "POST":
        form=AssignmentForm(request.POST,request.FILES)
        if form.is_valid():
            assign=form.save(commit=False)
            
            assign.save()
            send_mail_to_all_students_for_assignemt.delay(assign.id)  
            return redirect('home') 
        else:
            error(request, "Invalid assignment")
    return render(request,rf'assignements\create_assignment.html', {'form': form})
@login_required(login_url="login-page")
def assignement_home(request,class_id):
    classgroup=ClassGroup.objects.get(id=class_id)
    assignments=Assignment.objects.filter(classgroup=classgroup) 
    content={'assignments': assignments} 
    return render(request,rf'assignements\assignemts_home.html',content)  
def assignments_checking(request,class_id):
    classgroup=ClassGroup.objects.get(id=class_id)
    students=Student.objects.filter(classgroup=classgroup)
    student_assignment = []
    content={"students":students,"classgroup":classgroup}
    return render(request,rf"assignements\check_assignment.html",content)
    

def assignements_of_all_students(request,id):
    assignment=Assignment.objects.get(id=id)
    classgroup=assignment.classgroup
    all_students_in_class=Student.objects.filter(classgroup=classgroup)
    students_assignement=[]
    today=datetime.now().date()
    
    for student in all_students_in_class:
        assignements_exists=AssignmentSubmission.objects.filter(
            assignment=assignment,
            student=student,
        ).exists()
        students_assignement.append((student,assignements_exists))
    content={"students_assignement":students_assignement,"assignment":assignment,
             "classgroup":classgroup,"today":today}
    return render(request,"assignements/assignment_checking.html",content)
# C:\Users\Vijay\python pro\attendance2\templates\assignements/assignment_checking.html
        
    
from django.http import JsonResponse

def check_assignment(request, studentid, assignmentid):
    student = get_object_or_404(Student, id=studentid)
    assignment = get_object_or_404(Assignment, id=assignmentid)

    # Check the values before querying
    print(f"Student: {student}, Assignment: {assignment}")
    date_today=datetime.now().date()
    assgnemnt_subm, created = AssignmentSubmission.objects.get_or_create(
        student=student,
        assignment=assignment,
        submitted_date=date_today
        # Ensure dates or other fields are passed correctly
    )
    return JsonResponse({"status": "success", "data": {"check_ass"