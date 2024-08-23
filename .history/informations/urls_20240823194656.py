from django.urls import path
from . import views
urlpatterns = [
   path("all-classes-informations/",views.all_classes,name="all-classes-assignements"),
    path("all-year-assignements/<int:class_id>/",views.all_year_list,name="all-year-assignements"),
]

