from . import views
from django.urls import path

urlpatterns = [
    path("admin-panel/",views.admin_panel),
]
