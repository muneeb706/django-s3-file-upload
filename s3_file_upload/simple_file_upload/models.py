from django.db import models

UPLOAD_STATUS_CHOICES = (
    ("notstarted", "Not Started"),
    ("inprogress", "In Progress"),
    ("done", "Done")
)


class File(models.Model):
    path = models.FileField(upload_to="files")
    upload_status = models.CharField(max_length=50, choices=UPLOAD_STATUS_CHOICES)

