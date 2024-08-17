from django.urls import path
from . import views

urlpatterns = [
    path("all-classes-timetable/",views.all_classes,name="all-classes-timetable"),
    path('class-timetable/<str:classid>/',views.class_timetable,name="class-timetable"),
    path("create-timetabel"),

]
