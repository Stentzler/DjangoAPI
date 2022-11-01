from django.db import models
import uuid


class Exams(models.Model):
    id = models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True)
    name = models.CharField(max_length=66)
    subject = models.ForeignKey(
        "subjects.Subject", related_name="exams", on_delete=models.CASCADE
    )
    student = models.ForeignKey(
        "custom_users.Student", related_name="exams", on_delete=models.CASCADE
    )
    report_card = models.ForeignKey(
        "report_cards.ReportCard", related_name="exams", on_delete=models.CASCADE
    )
