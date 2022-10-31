from django.db import models
import uuid
# Create your models here.


class Exams(models.Model):
    id = models.UUIDField(default=uuid.uuid4, editable=False,
                          primary_key=True)
    name = models.CharField()
    subject = models.ForeignKey(
        "subjects.Subject", related_name="exams", on_delete=models.CASCADE)
    student = models.ForeignKey(
        "students.Student", related_name="exams", on_delete=models.CASCADE)
    report_card = models.ForeignKey(
        "report_cards.ReportCard", related_name="exams", on_delete=models.CASCADE)
