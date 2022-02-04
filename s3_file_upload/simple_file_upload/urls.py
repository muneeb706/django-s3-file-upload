from django.urls import path

from . import views

urlpatterns = [
    path("", views.SimpleFileUploadView.as_view(), name="file_upload"),
    path("progress", views.progress, name="file_upload_progress")
]