from .models import Student,Attendance
from faker import Faker # type: ignore 
from django.core.mail import send_mail 
from django.contrib.auth.models import User
from .models import Teacher ,CustomUser ,Student 
from django.conf import settings 
from time import sleep

import pandas as pd
from django.core.management.base import BaseCommand
from students.models import Student, Subject ,CustomUser

class Command(BaseCommand):
    help = 'Import student data from an Excel file'

    def add_arguments(self, parser):
        parser.add_argument('file_path', type=str, help='The path to the Excel file')

    def handle(self, *args, **kwargs):
        file_path = kwargs[rf'students\Copy of BBA_(COM)_24.25(1).xlsx']
        try:
            # Read the Excel file
            df = pd.read_excel(file_path)

            # Iterate over the rows in the DataFrame and create Student objects
            for index, row in df.iterrows():
                # Retrieve or create the associated CustomUser object
                fake=Faker()

                # Create the student object
                student = Student.objects.create(
                    roll_no=row['roll_no'],
                    name=row['name'],
                    email=fake.email(),
                    contact=fake.phone_number(),
                )

                # Associate subjects with the student
                subject_names = row['subjects'].split(',')  # Assuming subjects are comma-separated
                for subject_name in subject_names:
                    subject, _ = Subject.objects.get_or_create(name=subject_name.strip())
                    student.subject.add(subject)

                student.save()

            self.stdout.write(self.style.SUCCESS('Successfully imported student data'))

        except Exception as e:
            self.stdout.write(self.style.ERROR(f'Error importing student data: {e}'))
def fakestudents(count):
    fake=Faker()
    for _ in range(0,count):
        studets=Student.objects.create(
            name=fake.name()
        )
        studets.save()
        
def teaches_to_send_mail(subject,email_content):
    sender=settings.EMAIL_HOST_USER
    teachers=Teacher.objects.all()
    arr=[] 
    for teacher in teachers:
        receiver_email=teacher.user.email 
        try:
            # sleep(5)
            print(receiver_email ,"Wait")
            send_mail(subject,email_content,sender,[receiver_email])
            print(receiver_email,"Done")
        except Exception as e:
            print(e) 
            
def student_to_send_mail(id,subject,email_content):
    sender=settings.EMAIL_HOST_USER
    student=Student.objects.get(id=id)
    receiver_email=student.user.email
    try:
        # sleep(5)
        print(receiver_email ,"Wait")
        send_mail(subject,email_content,sender,[receiver_email])
        print(receiver_email,"Done")
    except Exception as e:
        print(e) 
    

def students_to_send_mail(subject,email_content):
    sender=settings.EMAIL_HOST_USER
    student=Student.objects.all()
    arr=[] 
    for std in student:
        if receiver_email:=std.user.email is None :
            return 'user does not have email'
         
        try:
            # sleep(5)
            print(receiver_email ,"Wait")
            send_mail(subject,email_content,sender,[receiver_email])
            print(receiver_email,"Done")
        except Exception as e:
            print(e)     
def faker_students(lenth):
    fake=Faker()
    
    for i in range(lenth):
        user=CustomUser.objects.create(
        username=fake.name(),
        email=fake.email(),
            password=fake.password(length=10),
            user_type=1,
        )
        
        Student.objects.create(
    user=user,
        name=fake.name(),
        contact=fake.phone_number(),
        
           profile=fake.image_url()
        )
            
            
        