from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
urlpatterns = [
    path("",views.home,name="home"),
    path("attendance/<str:pk>/",views.student_list,name="attendance-list"),
    path('mark/<int:student_id>/', views.mark_attendance, name='mark_attendance'),
path('apsent/<int:student_id>/', views.mark_apsent,name="apsent"),
path('create-subject/',views.create_subjescts,name="create-subject"),
path('teacher-data/',views.teacher_list,name="teacher-data"),
path('send-mail-teaches/',views.send_mails_to_teachers,name="send-mail-teaches"),
path('send-mail-students/',views.send_mails_to_all_students,name="send-mail-students"),
path('id-card/<str:id>/',views.id_card,name="id-card"),
path('send-mail-student/<str:id>/',views.send_mails_to_students,name="send-mail-student"),
    path('download-id-card/<int:student_id>/', views.download_id_card, name='download_id_card'),
path('attendance-data/<str:pk>/',views.attendance_data_students,name='attendance-data'), 
path('delete-student/<str:id>/<str:class_id>/',views.delete_student,name="delete-student"),
path("export_data_exel/<str:class_id>/",views.export_data_excel,name="expord-data"),
] 
if settings.DEBUG:  
    urlpatterns+=static(settings.MEDIA_URL,
                        document_root =settings.MEDIA_ROOT)
