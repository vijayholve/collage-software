from django.urls import path
from . import views

urlpatterns = [
path('create-feedback/',views.create_feedback,name="create-feedback"),
path('list-feedbacks',views.list_feedbacks,name="list-feedbacks"),
]
