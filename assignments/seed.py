from django.core.mail import send_mail 
from django.contrib.auth.models import User
from students.models import Assignment ,ClassGroup ,Student
from django.conf import settings 

def assignement_have_to_send_msg(id):
    sender=settings.EMAIL_HOST_USER
    assignment=Assignment.objects.get(id=id)
    classgroup=ClassGroup.objects.get(id=assignment.classgroup.id)
    students=Student.objects.filter(classgroup=classgroup)
    arr=[] 
    subject="New Assignement"
    email_content=f"""
    new assignemts is {assignment.title}
    class: {assignment.classgroup.name}
    year: {assignment.classgroup.year}
    start date: {assignment.assigned_date}
    end date: {assignment.due_date}
    link: http://127.0.0.1:8000/assignement/home-assignemts/
      
      please complete YOur assignement
    
    """
    for std in students:
        if receiver_email:=std.email is None :
            return 'user does not have email'
         
        try:
            # sleep(5)
            print(receiver_email ,"Wait")
            send_mail(subject,email_content,sender,[receiver_email])
            print(receiver_email,"Done")
        except Exception as e:
            print(e)    