from django.urls import path
from . import views

urlpatterns = [
        path("all-classes-assignements/",views.all_classes,name="all-classes-assignements"),

]
