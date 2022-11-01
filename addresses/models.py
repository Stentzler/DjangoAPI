from django.db import models
import uuid

class Address(models.Model):
    id = models.UUIDField(default=uuid.uuid4, primary_key=True, editable=False)
    zipcode = models.CharField(max_length=8)
    district = models.CharField(max_length=50)
    state = models.CharField(max_length =100)
    street = models.CharField(max_length =200)
    number = models.CharField(max_length =10)
