from django.test import TestCase
from model_bakery import baker
from django.db import IntegrityError
import ipdb

class ReportCardModelTest(TestCase):
    @classmethod
    def setUpTestData(cls) -> None:
        ...
        
    def setUp(self):
        self.student = baker.make("custom_users.Student")
    
    def test_can_create_a_proper_report_card(self):
        report_card = baker.make_recipe("report_cards.tests.report_card_custom", student=self.student)

        self.assertEqual(report_card.N1, 90)
        self.assertEqual(report_card.N2, 40)
        self.assertEqual(report_card.N3, 50)
        self.assertEqual(report_card.N4, 70)
        
        # Boolean fields should be set to False when not informed
        self.assertEqual(report_card.is_approved, False)
        self.assertEqual(report_card.is_active, False)
    
    def test_should_not_be_able_to_have_a_negative_score_N1(self):
        with self.assertRaises(IntegrityError):
            report_1 = baker.make("report_cards.ReportCard", N1=-30)
        
    def test_should_not_be_able_to_have_a_negative_score_N2(self):
        with self.assertRaises(IntegrityError):
            report_1 = baker.make("report_cards.ReportCard", N2=-20)
        
    def test_should_not_be_able_to_have_a_negative_score_N3(self):
        with self.assertRaises(IntegrityError):
            report_1 = baker.make("report_cards.ReportCard", N3=-60)
        
    def test_should_not_be_able_to_have_a_negative_score_N4(self):
        with self.assertRaises(IntegrityError):
            report_1 = baker.make("report_cards.ReportCard", N4=-10)
        
    def test_many_to_one_relation_with_student(self):
        reports = baker.make("report_cards.ReportCard", student=self.student , _quantity=10)

        self.assertEqual(self.student.report_cards.count(), 10)