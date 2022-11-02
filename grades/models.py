from django.db import models
import uuid


class Grade(models.Model):
    class Period(models.TextChoices):
        MANHA = "MANHÃ", "Matutino"
        TARDE = "TARDE", "Vespertino"
        NOITE = "NOITE", "Noturno"

    id = models.UUIDField(default=uuid.uuid4, primary_key=True, editable=False)
    period = models.CharField(
        max_length=20, choices=Period.choices, default=Period.MANHA
    )
    class_name = models.CharField(max_length=30, null=False, blank=False)
    grade = models.CharField(max_length=30, null=False, blank=False)

    subjects = models.ManyToManyField(
        "subjects.Subject",
        related_name="grades",
    )
