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
from django.db.models import Q
from django import template
import pandas as pd
from openpyxl import load_workbook


from django.http import FileResponse, Http404 ,HttpResponse 

register = template.Library()
@register.filter
def get_item(dictionary, key):
    return dictionary.get(key)
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
    content={'assignments': assignments,"classgroup":classgroup} 
    return render(request,rf'assignements\assignemts_home.html',content)  
@login_required(login_url="login-page")
def assignement_student_home_profile(request,sid):
    student=Student.objects.get(id=sid)
    classgroup=student.classgroup 
    assignments=Assignment.objects.filter(classgroup=classgroup)
    assignment_status_student=[]
    for ass in assignments:
        assignment_status=AssignmentSubmission.objects.filter(
            Q(assignment=ass) & 
            Q(student=student)
        ).exists()
        assignment_status_student.append((ass,assignment_status))
    content={'assignments': assignments,"assignment_status_student":assignment_status_student
             } 
    return render(request,rf'assignements\assignemt_student_home.html',content)


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
        submitted_date=date_today,
        status=True 
    )
    return redirect('home')

def assignment_table(request, id):
    classgroup = ClassGroup.objects.get(id=id)
    assignments = Assignment.objects.filter(classgroup=classgroup)
    students = Student.objects.filter(classgroup=classgroup)
    
    students_assignments = {}
    
    for std in students:
        students_assignments[std.id] = {}
        for ass in assignments:
            assignment_exist = AssignmentSubmission.objects.filter(
                Q(student=std) & Q(assignment=ass)
            ).exists()
            students_assignments[std.id][ass.id] = assignment_exist

    content = {
        'assignments': assignments,
        "classgroup":classgroup,
        'students': students, 
        'students_assignments': students_assignments,
    }
    return render(request, "assignements/assignments_table_students.html", content)
# C:\Users\Vijay\python pro\attendance2\templates\assignements\assignments_table_students.html


def export_data_excel(request, class_id):
    classgroup = ClassGroup.objects.get(id=class_id)

    end_date = datetime.now().date()
    start_date = end_date - timedelta(days=30)
    students = Student.objects.filter(classgroup=classgroup)
    data = []
    dates = 
    for student in students:
        row = {
            'Student ID': student.roll_no,
            'Name': student.name,
        }
        for date in dates:
            if date.weekday() == 6:  # Sunday
                row[date.strftime('%Y-%m-%d')] = '------'
            else:
                attendance = Attendance.objects.filter(student=student, date=date).first()
                row[date.strftime('%Y-%m-%d')] = 'Present' if attendance and attendance.present else 'Absent'
        data.append(row)
    
    df = pd.DataFrame(data)
    
    # Create an Excel writer using pandas with openpyxl engine
    file_path = rf'students\management\{classgroup.name}-{classgroup.year}.xlsx'
    with pd.ExcelWriter(file_path, engine='openpyxl') as writer:
        df.to_excel(writer, index=False, sheet_name=f'{classgroup.name}-{classgroup.year} Attendance')
    
    # Load the workbook and select the active sheet
    workbook = load_workbook(file_path)
    sheet = workbook.active
    
    # Adjust column widths
    for column in sheet.columns:
        max_length = 0
        column_name = column[0].column_letter
        for cell in column:
            try:
                if len(str(cell.value)) > max_length:
                    max_length = len(str(cell.value))
            except:
                pass
        adjusted_width = (max_length + 2)
        sheet.column_dimensions[column_name].width = adjusted_width
    
    workbook.save(file_path)
    
    if os.path.exists(file_path):
        with open(file_path, 'rb') as file:
            response = HttpResponse(file.read(), content_type='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet')
            response['Content-Disposition'] = f'attachment; filename={os.path.basename(file_path)}'
            return response
    else:
        raise Http404("File not found")
