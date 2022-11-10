from rest_framework.test import APITestCase
from subjects.models import Subject
from custom_users.models import User, Teacher, Student
from grades.models import Grade
from addresses.models import Address
from django.test import Client
from exams.models import Exams

class ExamsViewsTest(APITestCase):
    @classmethod
    def setUpTestData(cls) -> None:
        cls.address=Address.objects.create(**{
            "zipcode": "123523",
            "district": "Meio",
            "state": "RS",
            "street": "Rua",
            "number": "13A"
        })
        cls.address2=Address.objects.create(**{
            "zipcode": "123523",
            "district": "Meio",
            "state": "RS",
            "street": "Rua",
            "number": "13A"
        })
        cls.address3=Address.objects.create(**{
            "zipcode": "123523",
            "district": "Meio",
            "state": "RS",
            "street": "Rua",
            "number": "13A"
        })
        cls.teacher= Teacher.objects.create_user(**{
            "username": "teacher",
            "cpf": "999.999.999-99",
            "rg": "999-999-999",
            "first_name": "Stu",
            "last_name": "Dent",
            "age": 22,
            "contacts": "Dona Angela",
            "email":"student@mail.com",
            "password": "1234",
            "address":cls.address,
        })
        cls.subject= Subject.objects.create(**{"name":"materia1", "total_classes":20, "teacher":cls.teacher})
        cls.grade= Grade.objects.create(**{
            "class_name":"teste22", 
            "grade":"teste",
        })
        cls.grade.subjects.set([cls.subject.id])
        cls.student= Student.objects.create_user(**{
            "username": "student",
            "rg": "999-999-999",
            "first_name": "Stu",
            "last_name": "Dent",
            "age": 22,
            "contacts": "Dona Angela",
            "email":"student@mail.com",
            "password": "1234",
            "address":cls.address2,
            "grade":cls.grade
        })
        cls.exam_data={
            "subject": cls.subject.id,
            "quarter": "q4",
            "grades": cls.grade.id,
            "description": "Epa",
            "date": "2022-10-10"
        }
    
        cls.student.is_active=True
        cls.admin = User.objects.create_superuser(username="admin", password="12345", age=18, address=cls.address3, is_active=True )
        c= Client()
        verify = c.get(f"/api/teachers/verify/{cls.teacher.id}/")
        cls.teacher_token= c.post("/api/login/", {"username": "teacher", "password":"1234"}).data["token"]
        cls.admin_token= c.post("/api/login/", {"username":"admin", "password":"12345"}).data["token"]

    def test_teacher_can_create_exam(self):
        response_not_admin=self.client.post("/api/register/exams/", self.exam_data)
        self.assertEqual(response_not_admin.status_code, 401)
        self.client.credentials(HTTP_AUTHORIZATION='Token '+ self.teacher_token)
        response=self.client.post("/api/register/exams/", self.exam_data)
        self.assertEqual(response.status_code, 201)


    def test_only_admin_can_list_exams(self):
        response_not_admin=self.client.get("/api/exams/")
        self.assertEqual(response_not_admin.status_code, 401)
        self.client.credentials(HTTP_AUTHORIZATION='Token '+ self.admin_token)
        response=self.client.get("/api/exams/")
        self.assertEqual(response.status_code, 200)
        self.assertIsInstance(response.data, list)

    def test_only_admin_can_get_an_exam(self):
        self.client.credentials(HTTP_AUTHORIZATION='Token '+ self.teacher_token)
        response_create=self.client.post("/api/register/exams/", self.exam_data)
        exam= Exams.objects.get(subject=self.subject, student=self.student)
        self.client.credentials(HTTP_AUTHORIZATION='')
        response_not_admin=self.client.get(f'/api/exams/{exam.id}/')
        self.assertEqual(response_not_admin.status_code, 401)
        self.client.credentials(HTTP_AUTHORIZATION='Token '+ self.admin_token)
        response=self.client.get(f'/api/exams/{exam.id}/')
        self.assertEqual(response.status_code, 200)
        
    def test_only_teacher_can_delete_exam(self):
        self.client.credentials(HTTP_AUTHORIZATION='Token '+ self.teacher_token)
        response_create=self.client.post("/api/register/exams/", self.exam_data)
        exam= Exams.objects.get(subject=self.subject, student=self.student)
        self.client.credentials(HTTP_AUTHORIZATION='')
        response_not_admin= self.client.delete(f'/api/exams/{exam.id}/')
        self.assertEqual(response_not_admin.status_code, 401)
        self.client.credentials(HTTP_AUTHORIZATION='Token '+ self.teacher_token)
        response=self.client.delete(f'/api/exams/{exam.id}/')
        self.assertEqual(response.status_code, 204)
        
        
