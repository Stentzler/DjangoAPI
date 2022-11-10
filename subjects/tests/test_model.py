# from django.core.exceptions import ValidationError
from django.test import TestCase
from subjects.models import Subject
from custom_users.models import Teacher
from addresses.models import Address
import  uuid



class SubjectsTestCase(TestCase):
    @classmethod
    def setUpTestData(cls):
      cls.subject_data = {
        "name": "testSubject",
        "total_classes": 40
      }

      cls.teacher_data = {
        "username": "teacher01",
        "rg": "090-090-090",
        "first_name": "Luf",
        "last_name": "Jhon",
        "age": 22,
        "contacts": "Pedro",
        "email": "teacher01@mail.com",
        "password": "123456",
        "cpf": "09899965643",
      }

      cls.address_data = {
        "zipcode": "776545",
        "district": "Centro",
        "state": "BH",
        "street": "RuaE",
        "number": "766"
      }

      cls.address = Address.objects.create(**cls.address_data)
      cls.teacher = Teacher.objects.create(**cls.teacher_data, address = cls.address)


    def test_should_be_able_to_register_a_subjects(self):
        subject = Subject.objects.create(**self.subject_data,teacher=self.teacher)

        self.assertIsInstance(subject, Subject)
        self.assertIsInstance(subject.id, uuid.UUID)
        self.assertEqual(subject.name, self.subject_data["name"])
        self.assertEqual(subject.total_classes, self.subject_data["total_classes"])
        self.assertEqual(subject.teacher.id, self.teacher.id)
        self.assertEqual(subject.total_classes, 40)

      
    

       

  