from rest_framework.test import APITestCase
from subjects.models import Subject
from subjects.serializers import SubjectsSerializer
from custom_users.models import User
from addresses.models import Address
from django.test import Client

class SubjectViewsTest(APITestCase):
    @classmethod
    def setUpTestData(cls) -> None:
        cls.subject_data= {
            "name":"geografia",
            "total_classes": 10
        }
        cls.subject_instance= Subject.objects.create(**{
            "name":"matemagica",
            "total_classes": 22
        })
        cls.address= Address.objects.create(**{
            "zipcode": "123123",
            "district": "Centro",
            "state": "RS",
            "street": "Rua",
            "number": "123A"
	    })
        cls.admin = User.objects.create_superuser(username="admin", password="12345", age=18, address=cls.address, is_active=True )
        c= Client()
        cls.admin_token= c.post("/api/login/", {"username":"admin", "password":"12345"}).data["token"]

    def test_create_subject(self):
        self.client.credentials(HTTP_AUTHORIZATION='Token '+ self.admin_token)
        response= self.client.post('/api/register/subject/', self.subject_data)
        
        subject= Subject.objects.get(name=self.subject_data["name"])
        self.assertEqual(SubjectsSerializer(instance=subject).data, response.data)
        self.assertEqual(response.status_code, 201)

    def test_create_existing_subject(self):
        self.client.credentials(HTTP_AUTHORIZATION='Token '+ self.admin_token)
        response_one= self.client.post('/api/register/subject/', self.subject_data)
        response_two= self.client.post('/api/register/subject/', self.subject_data)
        self.assertEqual(response_two.status_code, 400)

    def test_only_admin_can_create_subject(self):
        response= self.client.post('/api/register/subject/', self.subject_data)
        self.assertEqual(response.status_code, 401)

    def test_only_admin_can_list_subjects(self):
        response_not_admin= self.client.get("/api/subjects/")
        self.assertEqual(response_not_admin.status_code, 401)
        self.client.credentials(HTTP_AUTHORIZATION='Token '+ self.admin_token)
        response= self.client.get("/api/subjects/")
        self.assertEqual(response.status_code, 200)
        self.assertIsInstance(response.data, list)
    
    def test_only_admin_can_get_one_subject(self):
        response_not_admin= self.client.get(f'/api/subjects/{self.subject_instance.id}/')
        self.assertEqual(response_not_admin.status_code, 401)
        self.client.credentials(HTTP_AUTHORIZATION='Token '+ self.admin_token)
        response= self.client.get(f'/api/subjects/{self.subject_instance.id}/')
        self.assertEqual(response.data, SubjectsSerializer(instance=self.subject_instance).data)
        self.assertEqual(response.status_code, 200)

    def test_only_admin_can_edit_subject(self):
        response_not_admin= self.client.patch(f'/api/subjects/{self.subject_instance.id}/', {"name":"fisica"})
        self.assertEqual(response_not_admin.status_code, 401)
        self.client.credentials(HTTP_AUTHORIZATION='Token '+ self.admin_token)
        response= self.client.patch(f'/api/subjects/{self.subject_instance.id}/', {"name":"fisica"})
        self.assertEqual(response.status_code, 200)
        
    def test_only_admin_can_delete(self):
        response_not_admin= self.client.delete(f'/api/subjects/{self.subject_instance.id}/')
        self.assertEqual(response_not_admin.status_code, 401)
        self.client.credentials(HTTP_AUTHORIZATION='Token '+ self.admin_token)
        response= self.client.delete(f'/api/subjects/{self.subject_instance.id}/', {"name":"fisica"})
        self.assertEqual(response.status_code, 204)
        
    
        
