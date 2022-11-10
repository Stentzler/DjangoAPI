from rest_framework.test import APITestCase
from custom_users.models import User, Student, Teacher
from addresses.models import Address
from django.test import Client
from .baker_recipes import student_custom, teacher_custom
from subjects.models import Subject
from grades.models import Grade
from rest_framework.authtoken.models import Token
from exams.models import Exams
import ipdb


class UserViewsTest(APITestCase):
    @classmethod
    def setUpTestData(cls) -> None:
        cls.teacher_data= teacher_custom.attr_mapping
        cls.subject= Subject.objects.create(**{"name":"materia1", "total_classes":20})
        cls.grade= Grade.objects.create(**{
            "class_name":"teste22", 
            "grade":"teste", 
        })
        cls.user_data= {
            "username": "student",
            "rg": "999-999-999",
            "first_name": "Stu",
            "last_name": "Dent",
            "age": 22,
            "contacts": "Dona Angela",
            "email":"student@mail.com",
            "password": "1234",
            "address":{
                "zipcode": "123523",
                "district": "Meio",
                "state": "RS",
                "street": "Rua",
                "number": "13A"
	        },
            "grade":cls.grade.id
        }
        cls.teacher_data= {
            "username": "teacher",
            "cpf": "999.999.999-99",
            "rg": "999-999-999",
            "first_name": "Stu",
            "last_name": "Dent",
            "age": 22,
            "contacts": "Dona Angela",
            "email":"student@mail.com",
            "password": "1234",
            "address":{
                "zipcode": "123523",
                "district": "Meio",
                "state": "RS",
                "street": "Rua",
                "number": "13A"
	        },
            "grade":cls.grade.id
        }
        cls.grade.subjects.set([cls.subject])
        cls.address_admin= Address.objects.create(**{
            "zipcode": "123123",
            "district": "Centro",
            "state": "RS",
            "street": "Rua",
            "number": "123A"
	    })

        cls.admin = User.objects.create_superuser(username="admin", password="12345", age=18, address=cls.address_admin, is_active=True )
        c= Client()
        cls.admin_token= c.post("/api/login/", {"username":"admin", "password":"12345"}).data["token"]
    
    def test_only_admin_can_create_student(self):
        response_not_admin= self.client.post("/api/register/student/", self.user_data, format="json")
        self.assertEqual(response_not_admin.status_code, 401)
        self.client.credentials(HTTP_AUTHORIZATION='Token '+ self.admin_token)
        response_admin= self.client.post("/api/register/student/", self.user_data, format="json")
        
        self.assertEqual(response_admin.status_code, 201)

    def test_only_admin_can_list_students(self):
        response_not_admin= self.client.get("/api/students/")
        self.assertEqual(response_not_admin.status_code, 401)
        self.client.credentials(HTTP_AUTHORIZATION='Token '+ self.admin_token)
        response_admin= self.client.get("/api/students/")
        self.assertEqual(response_admin.status_code, 200)
        self.assertIsInstance(response_admin.data,list)

    def test_only_admin_can_get_a_student(self):
        self.client.credentials(HTTP_AUTHORIZATION='Token '+ self.admin_token)
        create_response=self.client.post("/api/register/student/", self.user_data, format="json")
        self.client.credentials(HTTP_AUTHORIZATION='')
        response_not_admin= self.client.get(f'/api/students/{create_response.data["id"]}/')
        self.assertEqual(response_not_admin.status_code, 401)
        self.client.credentials(HTTP_AUTHORIZATION='Token '+ self.admin_token)
        response_admin= self.client.get(f'/api/students/{create_response.data["id"]}/')
        self.assertEqual(response_admin.status_code, 200)
        self.assertDictEqual(create_response.data, response_admin.data)

    def test_student_can_get_profile(self):
        self.client.credentials(HTTP_AUTHORIZATION='Token '+ self.admin_token)
        create_response=self.client.post("/api/register/student/", self.user_data, format="json")
        student= Student.objects.get(username=self.user_data["username"])
        student.is_active=True
        student.save()
        student_token= self.client.post("/api/login/", {"username":self.user_data["username"], "password":self.user_data["password"]}).data["token"]
        self.client.credentials(HTTP_AUTHORIZATION='Token '+student_token)
        response=self.client.get("/api/students/profile/")
        
        self.assertEqual(response.status_code, 200)

    def test_student_can_get_exams(self):
        self.client.credentials(HTTP_AUTHORIZATION='Token '+ self.admin_token)
        create_response=self.client.post("/api/register/student/", self.user_data, format="json")
        student= Student.objects.get(username=self.user_data["username"])
        student.is_active=True
        student.save()
        student_token= self.client.post("/api/login/", {"username":self.user_data["username"], "password":self.user_data["password"]}).data["token"]
        self.client.credentials(HTTP_AUTHORIZATION='Token '+student_token)
        response=self.client.get("/api/students/exams/")
        self.assertEqual(response.status_code, 200)
    
    def test_student_can_get_report_card(self):
        self.client.credentials(HTTP_AUTHORIZATION='Token '+ self.admin_token)
        create_response=self.client.post("/api/register/student/", self.user_data, format="json")
        student= Student.objects.get(username=self.user_data["username"])
        student.is_active=True
        student.save()
        student_token= self.client.post("/api/login/", {"username":self.user_data["username"], "password":self.user_data["password"]}).data["token"]
        self.client.credentials(HTTP_AUTHORIZATION='Token '+student_token)
        response=self.client.get("/api/students/report_card/")
        self.assertEqual(response.status_code, 200)

    def test_only_admin_can_update_student(self):
        
        self.client.credentials(HTTP_AUTHORIZATION='Token '+ self.admin_token)
        create_response=self.client.post("/api/register/student/", self.user_data, format="json")
        student= Student.objects.get(username=self.user_data["username"])
        student.is_active=True
        student.save()
        response=self.client.patch(f'/api/students/update/{student.id}/', {"username": "updated"})
        
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data["username"], "updated")
        self.client.credentials(HTTP_AUTHORIZATION='')
        response=self.client.patch(f'/api/students/update/{student.id}/', {"username": "not_updated"})
        self.assertEqual(response.status_code, 401)

    def test_only_admin_can_delete_student(self):
        self.client.credentials(HTTP_AUTHORIZATION='Token '+ self.admin_token)
        create_response=self.client.post("/api/register/student/", self.user_data, format="json")
        student= Student.objects.get(username=self.user_data["username"])
        student.is_active=True
        student.save()
        
        self.client.credentials(HTTP_AUTHORIZATION='')
        response_not_admin=self.client.delete(f'/api/students/{student.id}/')
        self.assertEqual(response_not_admin.status_code, 401)
        self.client.credentials(HTTP_AUTHORIZATION='Token '+ self.admin_token)
        response=self.client.delete(f'/api/students/{student.id}/')
        self.assertEqual(response.status_code, 204)
    
    def test_only_admin_can_create_teacher(self):
        self.client.credentials(HTTP_AUTHORIZATION='')
        response_not_admin= self.client.post("/api/register/teacher/", self.teacher_data, format="json")
        self.assertEqual(response_not_admin.status_code, 401)
        self.client.credentials(HTTP_AUTHORIZATION='Token '+ self.admin_token)
        response_admin= self.client.post("/api/register/teacher/", self.teacher_data, format="json")
        
        self.assertEqual(response_admin.status_code, 201)

    def test_only_admin_can_list_teachers(self):
        response_not_admin= self.client.get("/api/teachers/")
        self.assertEqual(response_not_admin.status_code, 401)
        self.client.credentials(HTTP_AUTHORIZATION='Token '+ self.admin_token)
        response_admin= self.client.get("/api/teachers/")
        self.assertEqual(response_admin.status_code, 200)
        self.assertIsInstance(response_admin.data,list)
    
    def test_only_admin_can_get_a_teacher(self):
        self.client.credentials(HTTP_AUTHORIZATION='Token '+ self.admin_token)
        
        create_response=self.client.post("/api/register/teacher/", self.teacher_data, format="json")
        self.client.credentials(HTTP_AUTHORIZATION='')
        response_not_admin= self.client.get(f'/api/teachers/{create_response.data["id"]}/')
        self.assertEqual(response_not_admin.status_code, 401)
        self.client.credentials(HTTP_AUTHORIZATION='Token '+ self.admin_token)
        response_admin= self.client.get(f'/api/teachers/{create_response.data["id"]}/')
        self.assertEqual(response_admin.status_code, 200)
        self.assertDictEqual(create_response.data, response_admin.data)

    def test_teacher_can_get_profile(self):
        self.client.credentials(HTTP_AUTHORIZATION='Token '+ self.admin_token)
        create_response=self.client.post("/api/register/teacher/", self.teacher_data, format="json")
        teacher= Teacher.objects.get(username=self.teacher_data["username"])
        teacher.is_active=True
        teacher.save()
        teacher_token= self.client.post("/api/login/", {"username":self.teacher_data["username"], "password":self.teacher_data["password"]}).data["token"]
        self.client.credentials(HTTP_AUTHORIZATION='Token '+teacher_token)
        response=self.client.get("/api/teacher/profile/")
        
        self.assertEqual(response.status_code, 200)
    
    def test_teacher_can_get_exams(self):
        self.client.credentials(HTTP_AUTHORIZATION='Token '+ self.admin_token)
        create_response=self.client.post("/api/register/teacher/", self.teacher_data, format="json")
        teacher= Teacher.objects.get(username=self.teacher_data["username"])
        teacher.is_active=True
        teacher.save()
        teacher_token= self.client.post("/api/login/", {"username":self.teacher_data["username"], "password":self.teacher_data["password"]}).data["token"]
        self.client.credentials(HTTP_AUTHORIZATION='Token '+teacher_token)
        response=self.client.get("/api/teacher/exams/")
        
        self.assertEqual(response.status_code, 200)
        self.assertIsInstance(response.data, list)

    def test_teacher_can_get_subjects(self):
        self.client.credentials(HTTP_AUTHORIZATION='Token '+ self.admin_token)
        create_response=self.client.post("/api/register/teacher/", self.teacher_data, format="json")
        teacher= Teacher.objects.get(username=self.teacher_data["username"])
        teacher.is_active=True
        teacher.save()
        subject= Subject.objects.create(**{"name":"nome", "total_classes":20, "teacher":teacher})
        teacher_token= self.client.post("/api/login/", {"username":self.teacher_data["username"], "password":self.teacher_data["password"]}).data["token"]
        self.client.credentials(HTTP_AUTHORIZATION='Token '+teacher_token)
        response=self.client.get("/api/teacher/subjects/")
        
        self.assertEqual(response.status_code, 200)
        self.assertIsInstance(response.data, list)

    def test_teacher_can_update_exam(self):
        self.client.credentials(HTTP_AUTHORIZATION='Token '+ self.admin_token)
        response_create_student = self.client.post("/api/register/student/", self.user_data, format="json")
        student= Student.objects.get(username=self.user_data["username"])
        student.is_active=True
        student.save()
        create_response=self.client.post("/api/register/teacher/", self.teacher_data, format="json")
        teacher= Teacher.objects.get(username=self.teacher_data["username"])
        teacher.is_active=True
        teacher.save()
        subject= Subject.objects.create(**{"name":"nome", "total_classes":20, "teacher":teacher})
        
        exam= Exams.objects.create(**{"subject":subject, "quarter":"q1", "description":"oioi", "date":"2022-10-10", "student":student})
        teacher_token= self.client.post("/api/login/", {"username":self.teacher_data["username"], "password":self.teacher_data["password"]}).data["token"]
        self.client.credentials(HTTP_AUTHORIZATION='Token '+teacher_token)
        response=self.client.patch(f'/api/exams/teacher/{exam.id}/', {"score":25, "description":"tchau tchau"})
        
        self.assertEqual(response.status_code, 200)

    def test_only_admin_can_update_teacher(self):
        
        self.client.credentials(HTTP_AUTHORIZATION='Token '+ self.admin_token)
        create_response=self.client.post("/api/register/teacher/", self.teacher_data, format="json")
        teacher= Teacher.objects.get(username=self.teacher_data["username"])
        teacher.is_active=True
        teacher.save()
        response=self.client.patch(f'/api/teachers/update/{teacher.id}/', {"username": "updated"})
        
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data["username"], "updated")
        self.client.credentials(HTTP_AUTHORIZATION='')
        response=self.client.patch(f'/api/teachers/update/{teacher.id}/', {"username": "not_updated"})
        self.assertEqual(response.status_code, 401)

    def test_only_admin_can_delete_teacher(self):
        self.client.credentials(HTTP_AUTHORIZATION='Token '+ self.admin_token)
        create_response=self.client.post("/api/register/teacher/", self.teacher_data, format="json")
        teacher= Teacher.objects.get(username=self.teacher_data["username"])
        teacher.is_active=True
        teacher.save()
        
        self.client.credentials(HTTP_AUTHORIZATION='')
        response_not_admin=self.client.delete(f'/api/teachers/{teacher.id}/')
        self.assertEqual(response_not_admin.status_code, 401)
        self.client.credentials(HTTP_AUTHORIZATION='Token '+ self.admin_token)
        response=self.client.delete(f'/api/teachers/{teacher.id}/')
        self.assertEqual(response.status_code, 204)