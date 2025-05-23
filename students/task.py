# your_app/tasks.py
from celery import shared_task
from django.core.mail import send_mail
from django.utils import timezone
from students.models import Attendance, Student

from celery import shared_task 
from .seed import student_to_send_mail,teaches_to_send_mail ,students_to_send_mail
import datetime
from django.conf import settings 

@shared_task(bind=True)
def send_mail_task(self,id,subject,mail_text):
    student_to_send_mail(id,subject,mail_text)
    times=datetime.datetime.now()
    current_time = times.strftime("%Y-%m-%d %H:%M:%S")
    return f"procced at {current_time} "

@shared_task(bind=True)
def send_mail_to_all_task_teacher(self,subject,mail_text):
    teaches_to_send_mail(subject,mail_text)
    return "done"

@shared_task(bind=True)
def send_mail_to_all_task_students(self,subject,mail_text,classid):
    students_to_send_mail(subject,mail_text,classid)
    return "done"

@shared_task(bind=True)
def hello(self):
    for i in range(1,10):
        print("hello",i)
@shared_task(bind=True)
def send_absence_emails(self):
    today = timezone.now().date()
    all_students = Student.objects.all()
    
    # Mark students absent if they are not listed for today
    for student in all_students:
        if not Attendance.objects.filter(student=student, date=today).exists():
            Attendance.objects.create(student=student, date=today, present=False)
    
    absentees = Attendance.objects.filter(date=today, present=False)
    
    # Send email absent students
    for record in absentees:
        student = record.student
        subject = 'Attendance Notification'  
        content = f'Dear {student.name},\n\nYou were marked absent for the subject on {today}. Please contact your teacher if this is a mistake.'  # Make sure this is a string, not a tuple
        
        if student.user:
            send_mail(
                subject,
                content,
                settings.EMAIL_HOST_USER,
                [student.user.email],
            )
           
    
    print(f"Sent absence notifications to {absentees.count()} students for {today}")
