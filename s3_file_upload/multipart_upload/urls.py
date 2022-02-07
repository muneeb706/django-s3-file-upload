from django.urls import path

from . import views

urlpatterns = [
    path("", views.MultipartUploadView.as_view(), name="multipart_upload"),
    path("progress", views.progress, name="file_upload_progress")
]
