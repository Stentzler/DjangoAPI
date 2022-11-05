from django.core.management.base import BaseCommand
from subjects.models import Subject
from custom_users.models import Teacher
from addresses.models import Address
# from django.utils.crypto import get_random_string

class Command(BaseCommand):
    help = 'Create subjects'

    def handle(self, *args, **kwargs):
        base_teacher = {
            "username": "testeacher",
            "first_name": "test",
            "last_name": "teacher",
            "age": 30,
            "email": "teacher@test.com",
            "password": "123321",
            "rg": "42527013",
            "cpf": "29144328719",
            "contacts": "test contact"
        }
        
        base_address = {
            "zipcode": "40800570",
            "district": "Salvador",
            "state": "Bahia",
            "street": "Estrada da Base Naval de Aratu",
            "number": "783"
        }

        base_subjects = ["mathematics", "history", "physics", "biology", "chemistry", "geography", "philosophy", "physical education", "art"]

        address, _ = Address.objects.get_or_create(**base_address)
        teacher, _ = Teacher.objects.get_or_create(**base_teacher, address=address)

        for subject in base_subjects:
            Subject.objects.create(
                name=subject,
                teacher=teacher
            )