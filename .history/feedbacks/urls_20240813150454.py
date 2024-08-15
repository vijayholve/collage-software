from django.urls import path
from . import views

urlpatterns = [
path('create-feedback/',views.create_feedback,name="create-feedback"),
path('create-categerory-feedback/',views.create_categerory,name="create-categerory-feedback"),
path('categerory-feedback/<str:category_id>/',views.feedback_by_category,name="categerory-feedback"),
path('list-feedbacks',views.list_feedbacks,name="list-feedbacks"),
path('submit-feedbacks/<str:category_id>/',views.submit_feedback,name="submit-feedbacks"),
path('add-feedback-quistions/<str:',views.add_question,name="add-feedback-quistions"),
]
