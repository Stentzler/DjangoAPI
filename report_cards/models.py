from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator 

import uuid

class ReportCard(models.Model):
    id = models.UUIDField(default=uuid.uuid4, primary_key=True, editable=False)
    result_q1 = models.PositiveIntegerField(default=0, validators=[ MinValueValidator(0), MaxValueValidator(100)])
    result_q2 = models.PositiveIntegerField(default=0, validators=[ MinValueValidator(0), MaxValueValidator(100)])
    result_q3 = models.PositiveIntegerField(default=0, validators=[ MinValueValidator(0), MaxValueValidator(100)])
    result_q4 = models.PositiveIntegerField(default=0, validators=[ MinValueValidator(0), MaxValueValidator(100)])
    is_approved = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    average = models.DecimalField(default=0, max_digits=5, decimal_places=2)
    absences = models.PositiveIntegerField(default=0)
    attendance = models.DecimalField(default=100.00, max_digits=5, decimal_places=2)

    student = models.ForeignKey("custom_users.Student", on_delete=models.CASCADE, related_name="report_cards")
    subject = models.ForeignKey("subjects.Subject", on_delete=models.CASCADE)
    
   

    