from django.urls import path 
from . import views
urlpatterns = [
    path("all-classes-assignements/",views.all_classes,name="all-classes-assignements"),
    path("all-year-assignements/<int:class_id>/",views.all_year_list,name="all-year-assignements"),
    path('create-assignment/',views.assignemt_form,name="create-assignment"),
    path('home-assignemts/<str:class_id>/',views.assignement_home,name="home-assignemts"),
    path('download/<int:file_id>/', views.download_file, name='download_file'),
    path('assignment-checking/<int:class_id>/', views.assignments_checking, 
         name='assignment-checking'),
    # path("/check-assignment/${studentId}/",views.che)

    
 
]
