from django.urls import path
from . import views
urlpatterns = [
   path("all-classes-information/",views.all_classes,name="all-classes-information"),
    path("class-information/<int:class_id>/",views.class_information,name="class-informations"),
path('delete-student/<str:id>/<str:class_id>/',views.delete_student,name="delete-student"),

]

