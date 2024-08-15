from django.urls import path
from . import views

urlpatterns = [
path('create-feedback/',views.create_feedback,name="create-feedback"),
 {
        'category': category,
        'questions': questions,
        'responses': responses
    }
path('list-feedbacks',views.list_feedbacks,name="list-feedbacks"),
path('add-feedback-quistions/',views.add_question,name="add-feedback-quistions"),
]
