from django.db import models
import uuid
from django.core.validators import MaxValueValidator, MinValueValidator



    

class Exams(models.Model):
    class QuarterOptions(models.TextChoices):
        Q1="q1"
        Q2="q2"
        Q3="q3"
        Q4="q4"
        
    
    
    id = models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True)
    score = models.PositiveIntegerField(
        default=0, validators=[MinValueValidator(0), MaxValueValidator(100)])
    description=models.TextField()
    date=models.DateField()
    quarter= models.TextField(choices=QuarterOptions.choices)
    subject = models.ForeignKey(
        "subjects.Subject", related_name="exams", on_delete=models.CASCADE
    )
    student = models.ForeignKey(
        "custom_users.Student", related_name="exams", on_delete=models.CASCADE
    )
    report_card = models.ForeignKey(
         "report_cards.ReportCard", related_name="exams", on_delete=models.CASCADE, null=True
    )
