from django.db import models
import uuid
from django.core.validators import MaxValueValidator, MinValueValidator


class Exams(models.Model):
    id = models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True)
    score = models.PositiveIntegerField(
        default=0, validators=[MinValueValidator(0), MaxValueValidator(100)])
    subject = models.ForeignKey(
        "subjects.Subject", related_name="exams", on_delete=models.CASCADE
    )
    student = models.ForeignKey(
        "custom_users.Student", related_name="exams", on_delete=models.CASCADE
    )
    
