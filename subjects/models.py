from django.db import models
import uuid

class Subject(models.Model):
    id = models.UUIDField(default=uuid.uuid4, primary_key=True, editable=False)
    name = models.CharField(max_length=50, unique=True)

    teacher = models.ForeignKey(
        "custom_users.Teacher", on_delete=models.CASCADE, related_name="Subjects"
    )
