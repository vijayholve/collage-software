from django.urls import path
from . import views

urlpatterns = [
    path("create-classes/",views.create_classes,name="create-classes"),
        path("all-classes/",views.classes_list,name="all-classes"),

] 
