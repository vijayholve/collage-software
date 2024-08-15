from django.urls import path
from . import views


urlpatterns = [
    path('exam-create/',views.create_exams,name='exam-create'),
    path('exam-home/',views.home_exams,name='exam-home'),
        path('update-exam/<str:test_id>/',views.update_exams,name='update-exam'),
    path('delete-exam/<str:exam_id>/',views.delete_exam,name="delete-exam"),
    path('add_question/<int:test_id>/', views.add_question, name='add_question'),
    path('test-detail/<int:pk>/', views.test_detail, name='test_detail'),
    path('take_test/<int:test_id>/', views.take_test, name='take_test'),
    path("students-results/<str:test_id>/",views.students_result_exam,name="students-results"),
    path(''update-quistion'/<str:quistion_id>/',views.update_quistion,name="update-quistion"),
    path('delete-quistion/<str:id>/',views.quistion_delete,name="delete-quistion"),
    path('delete-option/<str:id>/<str:test_id>/',views.option_delete,name="delete-option"),
]

