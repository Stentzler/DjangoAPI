from django.db import models
import uuid
# Create your models here.


class Exams(models.Model):
    id = models.UUIDField(default=uuid.uuid4, editable=False,
                          null=False, primary_key=True, unique=True)
    name = models.CharField()
    subjects = models.ForeignKey(
        "subjects.Subject", related_name="exams", on_delete=models.CASCADE)
    students = models.ForeignKey(
        "students.Student", related_name="exams", on_delete=models.CASCADE)
    report_cards = models.ForeignKey(
        "report_cards.ReportCard", related_name="exams", on_delete=models.CASCADE)
