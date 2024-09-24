from django.urls import path
from . import views
urlpatterns = [
   path("all-classes-information/",views.all_classes,name="all-classes-information"),
    path("class-information/<int:class_id>/",views.class_information,name="class-informations"),

]

