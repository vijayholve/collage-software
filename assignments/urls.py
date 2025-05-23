from django.urls import path 
from . import views
urlpatterns = [
    path("all-classes-assignements/",views.all_classes,name="all-classes-assignements"),
    path("all-year-assignements/<int:class_id>/",views.all_year_list,name="all-year-assignements"),
    path('create-assignment/',views.assignemt_form,name="create-assignment"),
    path('home-assignemts/<str:class_id>/',views.assignement_home,name="home-assignemts"),
    path('download/<int:file_id>/', views.download_file, name='download_file'),
    # path('assignment-checking/<int:class_id>/', views.assignments_checking, 
    #      name='assignment-checking'),
        path('assignement-checking/<int:id>/',views.assignements_of_all_students,name="assignment-checking"),
path('assignement/check/<int:studentid>/<int:assignmentid>/', views.check_assignment, name='check-assignment'),
path('your-assignment/<str:sid>/',views.assignement_student_home_profile,name="student-profile-assignement"),
path("students-assignement-table/<int:id>/",views.assignment_table,name="assignment-table"),
path('expot-data/<int:class_id>/',views.export_assignment_data_excel,name="export-assignment") 
]
