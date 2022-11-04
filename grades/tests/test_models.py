from django.test import TestCase
from model_bakery import baker
from grades.models import Grade
import ipdb

class GradesModelTest(TestCase):
    @classmethod
    def setUpTestData(cls) -> None:
        ...
    def setUp(self):
        """ self.student = baker.make("custom_users.Student")
        self.subject= baker.make("subjects.Subject") """
        self.subject= baker.make("subjects.Subject", _quantity=10)
       
        
    def test_period_max_lenght(self):
        """Checks if the maximum length of period is working correctly"""
        result_max_length_period= Grade._meta.get_field("period").max_length
        self.assertEqual(20,result_max_length_period)
   
        
    def test_class_name_max_lenght(self):
        """Checks if the max size of class_name is working correctly"""
        result_max_length_class_name= Grade._meta.get_field("class_name").max_length
        self.assertEqual(30,result_max_length_class_name)
      
        
    def test_grade_lenght(self):
       """Checks if the maximum size of grade is working correctly"""
       result_max_length_grade= Grade._meta.get_field("grade").max_length
       self.assertEqual(30,result_max_length_grade)
    
    """ def test_options_choices_corrects(self):
        "checks if create a grading with the correct period"
        c=[('MANHÃ', 'Matutino'), ('TARDE', 'Vespertino'), ('NOITE', 'Noturno')]
        grade1= baker.make("grades.Grade")
        print(grade1.period)
        for choices in c:
            if choices[0]==grade1.period:
                print("ok") """
             
    def test_many_to_many_relation_with_subjects(self):
        """checks many to many relation Grades with subjects"""
        grades = baker.make("grades.Grade", subjects=self.subject , _quantity=10)
        self.assertEqual(len(grades), 10) 
        self.assertEqual(len(self.subject), 10)
        
       
            
         
      