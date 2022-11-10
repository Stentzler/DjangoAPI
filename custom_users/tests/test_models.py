from django.test import TestCase
from custom_users.models import Student, Teacher
from model_bakery import baker
import datetime, uuid
import ipdb
from custom_users.tests.baker_recipes import student_custom, teacher_custom
from django.db import IntegrityError

class UsersModelTest(TestCase):
    def setUp(self):
        self.address = baker.make("addresses.Address")
        self.grade = baker.make("grades.Grade")
        self.base_user = baker.make("custom_users.Student")

    def test_should_be_able_to_register_a_student(self):
        """trying to create an student providing correct data"""
        student = baker.make_recipe("custom_users.tests.student_custom", address=self.address, grade=self.grade)
        student_base_data = student_custom.__dict__

        self.assertIsInstance(student, Student)
        self.assertIsInstance(student.id, uuid.UUID)
        self.assertIsInstance(student.date_joined, datetime.datetime)
        self.assertEqual(student.username, student_base_data["attr_mapping"]["username"])
        self.assertEqual(student.first_name, student_base_data["attr_mapping"]["first_name"])
        self.assertEqual(student.last_name, student_base_data["attr_mapping"]["last_name"])
        self.assertEqual(student.rg, student_base_data["attr_mapping"]["rg"])
        self.assertEqual(student.age, student_base_data["attr_mapping"]["age"])
        self.assertEqual(student.contacts, student_base_data["attr_mapping"]["contacts"])
        self.assertEqual(student.email, student_base_data["attr_mapping"]["email"])
        self.assertEqual(student.role, "STUDENT")
        self.assertEqual(student.address.id, self.address.id)
        self.assertEqual(student.grade.id, self.grade.id)
        self.assertFalse(student.is_active)
        self.assertFalse(student.is_superuser)
        self.assertFalse(student.is_staff)

    def test_should_be_able_to_register_a_teacher(self):
        """trying to create an student passing correct data"""
        teacher = baker.make_recipe("custom_users.tests.teacher_custom", address=self.address)
        teacher_base_data = teacher_custom.__dict__

        self.assertIsInstance(teacher, Teacher)
        self.assertIsInstance(teacher.id, uuid.UUID)
        self.assertIsInstance(teacher.date_joined, datetime.datetime)
        self.assertEqual(teacher.username, teacher_base_data["attr_mapping"]["username"])
        self.assertEqual(teacher.first_name, teacher_base_data["attr_mapping"]["first_name"])
        self.assertEqual(teacher.last_name, teacher_base_data["attr_mapping"]["last_name"])
        self.assertEqual(teacher.rg, teacher_base_data["attr_mapping"]["rg"])
        self.assertEqual(teacher.age, teacher_base_data["attr_mapping"]["age"])
        self.assertEqual(teacher.contacts, teacher_base_data["attr_mapping"]["contacts"])
        self.assertEqual(teacher.email, teacher_base_data["attr_mapping"]["email"])
        self.assertEqual(teacher.cpf, teacher_base_data["attr_mapping"]["cpf"])
        self.assertEqual(teacher.role, "TEACHER")
        self.assertEqual(teacher.address.id, self.address.id)
        self.assertFalse(teacher.is_active)
        self.assertFalse(teacher.is_superuser)
        self.assertFalse(teacher.is_staff)
    
    def test_user_username_max_length(self):
        max_length = self.base_user._meta.get_field('username').max_length

        self.assertEqual(max_length, 150)

    def test_user_first_name_max_length(self):
        max_length = self.base_user._meta.get_field('first_name').max_length

        self.assertEqual(max_length, 150)

    def test_user_last_name_max_length(self):
        max_length = self.base_user._meta.get_field('last_name').max_length

        self.assertEqual(max_length, 150)

    def test_user_role_max_length(self):
        max_length = self.base_user._meta.get_field('role').max_length

        self.assertEqual(max_length, 50)

    def test_user_contacts_max_length(self):
        max_length = self.base_user._meta.get_field('contacts').max_length

        self.assertEqual(max_length, 70)

    def test_user_password_max_length(self):
        max_length = self.base_user._meta.get_field('password').max_length

        self.assertEqual(max_length, 200)

    def test_user_rg_max_length(self):
        max_length = self.base_user._meta.get_field('rg').max_length

        self.assertEqual(max_length, 20)

    def test_user_age_does_not_accept_negative_values(self):
        with self.assertRaises(IntegrityError):
            baker.make("custom_users.Student", age=-34)




