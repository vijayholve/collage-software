from django.urls import path
from . import views

urlpatterns = [
path('create-feedback/',views.create_feedback,name="create-feedback"),
path('create-category-feedback/',views.create_categerory,name="create-categerory-feedback"),
path('category-feedback/<str:category_id>/',views.feedback_by_category,name="categerory-feedback"),
path('list-feedbacks',views.list_feedbacks,name="list-feedbacks"),
path('submit-feedbacks/<str:category_id>/',views.submit_feedback,name="submit-feedbacks"),
path('add-feedback-quistions/<str:category_id>/',views.add_question,name="add-feedback-quistions"),
]
