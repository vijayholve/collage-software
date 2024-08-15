from django.urls import path
from . import views

urlpatterns = [
    path("profile-detail/<str:sid>/",views.student_profile),
]
