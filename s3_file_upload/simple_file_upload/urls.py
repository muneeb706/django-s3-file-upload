from django.urls import path

from . import views

urlpatterns = [
    path("", views.SimpleFileUploadView.as_view())
]