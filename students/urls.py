from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
urlpatterns = [
    path("",views.home,name="home"),
    path("container/",views.container,name="container"),
    path("attendance/<str:pk>/",views.student_attendance_list,name="attendance-list"),
    path("attendance-one/<str:sid>/",views.particular_student_attendance,name="attendance-one"),
    path('mark/<int:student_id>/', views.mark_attendance, name='mark_attendance'),
path('apsent/<int:student_id>/', views.mark_apsent,name="apsent"),
path('create-subject/',views.create_subjescts,name="create-subject"),
path('teacher-data/',views.teacher_list,name="teacher-data"),
path('send-mail-teaches/',views.send_mails_to_teachers,name="send-mail-teaches"),
path('send-mail-students/<str:classid>/',views.send_mails_to_all_students,name="send-mail-students"),
path('id-card/<str:id>/',views.id_card,name="id-card"),
path('send-mail-student/<str:id>/',views.send_mails_to_students,name="send-mail-student"),
    path('download-id-card/<int:student_id>/', views.download_id_card, name='download_id_card'),
path('attendance-data/<str:pk>/',views.attendance_data_students,name='attendance-data'), 
path("export_data_exel/<str:class_id>/",views.export_data_excel,name="expord-data"),
path('attendance_export_date_form/<str:class_id>/',views.attendance_export_date_form,name="attendance_export_date_form"),
path('export_past_data_excel/<int:class_id>/<str:start_date>/<str:end_date>/', 
     views.export_past_data_excel, name='export_data_exel_past'),
path("import_exel_data/<str:classid>/",views.import_data,name="import-data"),
path('holidays/<str:classid>/',views.Holiday_page,name="holidays"),
path('create-holidays/',views.create_holiday,name="create-holidays"),

] 
if settings.DEBUG:  
    urlpatterns+=static(settings.MEDIA_URL,
                        document_root =settings.MEDIA_ROOT) 
