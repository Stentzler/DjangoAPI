from django.db import models
import uuid

class Grade(models.Model):
    id = models.UUIDField(default=uuid.uuid4, primary_key=True, editable=False)
    period = models.CharField(max_length=30, null=False, blank=False)
    grade = models.CharField(max_length=20, null=False, blank=False)
    class_name = models.CharField(max_length=30, null=False, blank=False)

    subjects = models.ManyToManyField(
        "subjects.Subject",
        related_name="grades",
    )
