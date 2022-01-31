from django.db import models

UPLOAD_STATUS_CHOICES = (
    ("notstarted", "Not Started"),
    ("inprogress", "In Progress"),
    ("done", "Done")
)


class Image(models.Model):
    file_path = models.ImageField(upload_to="images")
    upload_status = models.CharField(max_length=50, choices=UPLOAD_STATUS_CHOICES)

