from django.db import IntegrityError
from django.test import TestCase
from model_bakery import baker


class ExamsModelTest(TestCase):
    @classmethod
    def setUpTestData(cls) -> None:
        ...
    def setUp(self):
        self.student = baker.make("custom_users.Student")
        self.subject= baker.make("subjects.Subject")
       
        
    def test_should_not_be_able_to_have_a_negative_score(self):
        """checks that a negative score cannot be created"""
        with self.assertRaisesMessage(IntegrityError,"CHECK constraint failed: score"): 
           exam1=baker.make("exams.Exams",score= -20)
        
        
    def test_many_to_one_relation_with_students(self):
        """checks many to one relation exams with students"""
        exam3 = baker.make("exams.Exams", student=self.student , _quantity=10)
        self.assertEqual(self.student.exams.count(), 10)   
        
    def test_many_to_one_relation_with_subjects(self):
        """checks many to one relation exams with subjects"""
        exam4 = baker.make("exams.Exams", subject=self.subject , _quantity=10)
        self.assertEqual(self.subject.exams.count(), 10)     
       
                