from django.test import TestCase
from custom_users.models import Student, Teacher
from addresses.models import Address
from grades.models import Grade
import datetime, uuid


class UsersModelTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.address_data = {
            "zipcode": "123123",
            "district": "Centro",
            "state": "RS",
            "street": "Rua",
            "number": "123A",
        }

        cls.grade_data = {
            "class_name": "5a_A",
            "grade": "5a Série",
        }

        cls.student_data = {
            "username": "student",
            "rg": "999-999-999",
            "first_name": "Stu",
            "last_name": "Dent",
            "age": 22,
            "contacts": "Dona Angela",
            "email": "student@mail.com",
            "password": "1234",
        }

        cls.teacher_data = {
            "username": "teacher",
            "rg": "999-999-999",
            "first_name": "Tea",
            "last_name": "Cher",
            "age": 18,
            "contacts": "Dona Angela",
            "email": "teacher@mail.com",
            "password": "1234",
            "cpf": "12345678910",
        }

        cls.address = Address.objects.create(**cls.address_data)
        cls.grade = Grade.objects.create(**cls.grade_data)

    def test_should_be_able_to_register_a_student(self):
        """trying to create an student providing correct data"""
        student = Student.objects.create_user(
            **self.student_data, address=self.address, grade=self.grade
        )

        self.assertIsInstance(student, Student)
        self.assertIsInstance(student.id, uuid.UUID)
        self.assertIsInstance(student.date_joined, datetime.datetime)
        self.assertEqual(student.username, self.student_data["username"])
        self.assertEqual(student.first_name, self.student_data["first_name"])
        self.assertEqual(student.last_name, self.student_data["last_name"])
        self.assertEqual(student.rg, self.student_data["rg"])
        self.assertEqual(student.age, self.student_data["age"])
        self.assertEqual(student.contacts, self.student_data["contacts"])
        self.assertEqual(student.email, self.student_data["email"])
        self.assertEqual(student.role, "STUDENT")
        self.assertEqual(student.address.id, self.address.id)
        self.assertEqual(student.grade.id, self.grade.id)
        self.assertTrue(student.is_active)
        self.assertFalse(student.is_superuser)
        self.assertFalse(student.is_staff)

    def test_should_be_able_to_register_a_teacher(self):
        """trying to create an student passing correct data"""

        teacher = Teacher.objects.create_user(**self.teacher_data, address=self.address)

        self.assertIsInstance(teacher, Teacher)
        self.assertIsInstance(teacher.id, uuid.UUID)
        self.assertIsInstance(teacher.date_joined, datetime.datetime)
        self.assertEqual(teacher.username, self.teacher_data["username"])
        self.assertEqual(teacher.first_name, self.teacher_data["first_name"])
        self.assertEqual(teacher.last_name, self.teacher_data["last_name"])
        self.assertEqual(teacher.rg, self.teacher_data["rg"])
        self.assertEqual(teacher.age, self.teacher_data["age"])
        self.assertEqual(teacher.contacts, self.teacher_data["contacts"])
        self.assertEqual(teacher.email, self.teacher_data["email"])
        self.assertEqual(teacher.cpf, self.teacher_data["cpf"])
        self.assertEqual(teacher.role, "TEACHER")
        self.assertEqual(teacher.address.id, self.address.id)
        self.assertTrue(teacher.is_active)
        self.assertFalse(teacher.is_superuser)
        self.assertFalse(teacher.is_staff)
