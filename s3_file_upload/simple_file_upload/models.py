from django.db import models

UPLOAD_STATUS_CHOICES = (
    ("notstarted", "Not Started"),
    ("inprogress", "In Progress"),
    ("done", "Done")
)


class File(models.Model):
    #TODO: Briefly mention how file field works
    path = models.FileField(upload_to="simple_file_upload")