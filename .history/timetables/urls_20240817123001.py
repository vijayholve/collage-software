from django.urls import path
from . import views

urlpatterns = [
    path("all-classes-/",views.all_classes,name="all-classes-"),

]
