from django.urls import path
from . import views

urlpatterns = [
path('create-feedback/',views.create_feedback,name="create-feedback"),
path('create-categerory-feedback/',views.create_categerory,name="create-categerory-feedback"),
path('categerory-feedback/',views.feedback_by_category,name="categerory-feedback"),
path('list-feedbacks',views.list_feedbacks,name="list-feedbacks"),
path('add-feedback-quistions/<category_id>/',views.add_question,name="add-feedback-quistions"),
]
