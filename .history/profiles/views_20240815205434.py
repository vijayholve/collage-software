from django.shortcuts import render

# Create your views here.
def student_profile(request, sid):
    student = Student.objects.get(id=sid)
    context = {
        'student': student,
    }
    return render(request, 'students/student_profile.html', context)
