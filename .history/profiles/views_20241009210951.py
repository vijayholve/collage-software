from django.shortcuts import render
from students.models import Student,CustomUser
from django.views.decorators.cache import never_cache
from django.contrib.auth.decorators import login_required
# Create your views here.
@never_cache
@login_required(login_url='login-page')
def student_profile(request, sid):
    student = Student.objects.get(id=sid)
    context = {
        'student': student,
    }
    return render(request, 'profiles/student_profile.html', context)
