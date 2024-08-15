from django.contrib import admin
from django.urls import path ,include

urlpatterns = [
    path('admin/', admin.site.urls), 
    path('', include('students.urls')), 
    path('assignement/',include('assignments.urls')),
    path('account/', include('base.urls')),
    path('api/',include('api.urls')),
    path('exams/', include('exams.urls')),
    path('classes/',include('classes.urls')),
    path('feedbacks/',include('feedbacks.urls')),
    path('library/',include('library.urls')),
]

