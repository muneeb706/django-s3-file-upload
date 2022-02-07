from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path("simple-file-upload/", include("simple_file_upload.urls")),
    path("multipart-upload/", include("multipart_upload.urls"))
]