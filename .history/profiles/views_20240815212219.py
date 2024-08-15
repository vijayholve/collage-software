from django.shortcuts import render
from students.models import Student,CustomUser
# Create your views here.
def student_profile(request, sid):
    student = Student.objects.get(id=sid)
    context = {
        'student': student,
    }
        return render(request, 'profiles/student_profile.html', context)
