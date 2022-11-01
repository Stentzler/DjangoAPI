import uuid
from django.db import models
from django.contrib.auth.models import AbstractUser, BaseUserManager
from django.db.models.signals import post_save
from django.dispatch import receiver

from addresses.models import Address

# Caso seja criado um superUser pelo terminal será um Administrador
class User(AbstractUser):
    class Role(models.TextChoices):
        ADMIN = "ADMIN", "Admin"
        STUDENT = "STUDENT", "Student"
        TEACHER = "TEACHER", "Teacher"

    base_role = Role.ADMIN

    id = models.UUIDField(default=uuid.uuid4, primary_key=True, editable=False)
    role = models.CharField(max_length=50, choices=Role.choices)
    name = models.CharField(max_length=70)
    age = models.IntegerField()
    contacts = models.CharField(max_length=70)
    email = models.EmailField()
    password = models.CharField(max_length=70)
    rg = models.CharField(max_length=20)

    address = models.OneToOneField(Address, on_delete=models.CASCADE)

    def save(self, *args, **kwargs):
        self.role = self.base_role
        return super().save(*args, **kwargs)


# --------------------


class StudentManager(BaseUserManager):
    def get_queryset(self, *args, **kwargs):
        results = super().get_queryset(*args, **kwargs)
        return results.filter(role=User.Role.STUDENT)


class Student(User):

    base_role = User.Role.STUDENT

    student = StudentManager()

    class Meta:
        proxy = True


@receiver(post_save, sender=Student)
def create_user_profile(sender, instance, created, **kwargs):
    if created and instance.role == "STUDENT":
        StudentProfile.objects.create(user=instance)


class StudentProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)


# # -------------------


class TeacherManager(BaseUserManager):
    def get_queryset(self, *args, **kwargs):
        results = super().get_queryset(*args, **kwargs)
        return results.filter(role=User.Role.TEACHER)

class Teacher(User):

    base_role = User.Role.TEACHER

    teacher = TeacherManager()

    class Meta:
        proxy = True


class TeacherProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    teacher_id = models.IntegerField(null=True, blank=True)


@receiver(post_save, sender=Teacher)
def create_user_profile(sender, instance, created, **kwargs):
    if created and instance.role == "TEACHER":
        TeacherProfile.objects.create(user=instance)
