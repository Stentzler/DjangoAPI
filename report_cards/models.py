from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator 

import uuid

class ReportCard(models.Model):
    uuid = models.UUIDField(default=uuid.uuid4, primary_key=True, editable=False)
    N1 = models.PositiveIntegerField(default=0, validators=[ MinValueValidator(0), MaxValueValidator(100)])
    N2 = models.PositiveIntegerField(default=0, validators=[ MinValueValidator(0), MaxValueValidator(100)])
    N3 = models.PositiveIntegerField(default=0, validators=[ MinValueValidator(0), MaxValueValidator(100)])
    N4 = models.PositiveIntegerField(default=0, validators=[ MinValueValidator(0), MaxValueValidator(100)])
    is_approved = models.BooleanField(default=False)
    is_active = models.BooleanField(default=False)
    average = models.DecimalField(default=0, max_digits=5, decimal_places=2)
    attendance = models.DecimalField(default=100.00, max_digits=5, decimal_places=2)

    student = models.OneToOneField(..., on_delete=models.CASCADE)

    