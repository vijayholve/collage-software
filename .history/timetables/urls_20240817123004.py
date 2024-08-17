from django.urls import path
from . import views

urlpatterns = [
    path("all-classes-timeta/",views.all_classes,name="all-classes-timeta"),

]
