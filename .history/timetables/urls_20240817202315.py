from django.urls import path
from . import views

urlpatterns = [
    path("all-classes-timetable/",views.all_classes,name="all-classes-timetable"),
    path('class-timetable/<str:classgroup_id>/',views.class_timetable,name="class-timetable"),
    path("create-timetable/",views.create_timetable_of_class,name="create-timetable"),
        path('timetables/', timetable_list, name='timetable_list'),

]
