from django.urls import path 
from . import views

urlpatterns = [
    path('book-data/',views.library_home,name="book-data"),
    path("create-book/",views.books_form,name="create-book"),
    path("dowload-book/<str:file_id>/",views.download_file,name="dowload-book"), 
]