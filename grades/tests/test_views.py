from rest_framework.test import APITestCase
from subjects.models import Subject
from custom_users.models import User
from addresses.models import Address
from rest_framework.views import status
import ipdb

class GradeViewsTest(APITestCase):
    @classmethod
    def setUpTestData(cls) -> None:
        cls.subject_data = {
            "name": "history",
            "total_classes": 10
        }

        cls.subject_2_data = {
            "name": "biology",
            "total_classes": 22
        }

        cls.address= Address.objects.create(**{
            "zipcode": "123123",
            "district": "Centro",
            "state": "RS",
            "street": "Rua",
            "number": "123A"
	    })

        cls.admin = User.objects.create_superuser(username="admin", password="1234", age=18, address=cls.address, is_active=True )

    def setUp(self):
        self.admin_login = self.client.post("/api/login/", {"username": "admin", "password": "1234"}, format="json")
        self.admin_token = self.admin_login.data['token']
        self.client.credentials(HTTP_AUTHORIZATION='Token ' + self.admin_token)

        self.subject = self.client.post("/api/register/subject/", self.subject_data)
        self.subject_2 = self.client.post("/api/register/subject/", self.subject_2_data)

        self.grade_data = {
            "class_name":"5a_B", 
 	        "grade":"5a_serie",
	        "period": "TARDE",
 	        "subjects":
 	            [self.subject.data["id"]]
        }

    def test_should_be_able_to_register_a_new_grade(self):
        response = self.client.post("/api/register/grade/", self.grade_data, format="json")
        data = response.data

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(data["class_name"], self.grade_data["class_name"])
        self.assertEqual(data["grade"], self.grade_data["grade"])
        self.assertEqual(data["period"], self.grade_data["period"])
        self.assertEqual(len(data["subjects"]), 1)
        self.assertEqual(str(data["subjects"][0]), self.grade_data["subjects"][0])
    
    def test_should_be_able_to_register_a_grade_with_multiple_subjects(self):
        grade_data = {
            "class_name":"5a_B", 
 	        "grade":"5a_serie",
	        "period": "TARDE",
 	        "subjects":
 	            [self.subject.data["id"], self.subject_2.data["id"]]
        }

        response = self.client.post("/api/register/grade/", grade_data, format="json")
        data = response.data

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(len(data["subjects"]), 2)

    def test_should_not_be_able_to_register_two_grades_with_the_same_name(self):
        create_grade = self.client.post("/api/register/grade/", self.grade_data, format="json")

        response = self.client.post("/api/register/grade/", self.grade_data, format="json")
        
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_should_not_be_able_to_register_a_grade_if_not_admin(self):
        self.client.credentials(HTTP_AUTHORIZATION='Token 66bf30b712f0dcc3d9ce89eb5984d71b51499492')

        response = self.client.post("/api/register/grade/", self.grade_data, format="json")

        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_should_be_able_to_list_all_grades(self):
        grade_2_data = {
            "class_name":"5a_C", 
 	        "grade":"5a_serie",
	        "period": "TARDE",
 	        "subjects":
 	            [self.subject.data["id"]]
        }

        create_grade = self.client.post("/api/register/grade/", self.grade_data, format="json")
        create_second_grade = self.client.post("/api/register/grade/", grade_2_data, format="json")

        response = self.client.get("/api/grades/")

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 2)

    def test_should_not_be_able_to_list_all_grades_if_not_admin(self):
        grade_2_data = {
            "class_name":"5a_C", 
 	        "grade":"5a_serie",
	        "period": "TARDE",
 	        "subjects":
 	            [self.subject.data["id"]]
        }

        create_grade = self.client.post("/api/register/grade/", self.grade_data, format="json")
        create_second_grade = self.client.post("/api/register/grade/", grade_2_data, format="json")

        self.client.credentials(HTTP_AUTHORIZATION='Token 66bf30b712f0dcc3d9ce89eb5984d71b51499492')

        response = self.client.get("/api/grades/")

        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_should_be_able_to_list_a_specific_grade(self):
        create_grade = self.client.post("/api/register/grade/", self.grade_data, format="json")
        id = create_grade.data["id"]
        response = self.client.get(f"/api/grades/{id}/")

        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_should_not_be_able_to_list_a_specific_grade_if_not_admin(self):
        create_grade = self.client.post("/api/register/grade/", self.grade_data, format="json")
        id = create_grade.data["id"]

        self.client.credentials(HTTP_AUTHORIZATION='Token 66bf30b712f0dcc3d9ce89eb5984d71b51499492')

        response = self.client.get(f"/api/grades/{id}/")

        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_should_be_able_to_delete_a_grade(self):
        create_grade = self.client.post("/api/register/grade/", self.grade_data, format="json")
        id = create_grade.data["id"]
        response = self.client.delete(f"/api/grades/{id}/")

        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

    def test_should_not_be_able_to_delete_a_grade_if_not_admin(self):
        create_grade = self.client.post("/api/register/grade/", self.grade_data, format="json")
        id = create_grade.data["id"]

        self.client.credentials(HTTP_AUTHORIZATION='Token 66bf30b712f0dcc3d9ce89eb5984d71b51499492')

        response = self.client.delete(f"/api/grades/{id}/")

        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)
