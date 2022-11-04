from rest_framework import serializers
from exams.models import Exams
from report_cards.serializers import ReportCardSerializer
from custom_users.serializers import StudentSerializer
from subjects.serializers import SubjectsSerializer


class ExamsSerializer(serializers.ModelSerializer):
    student = StudentSerializer(many=True)
    subject = SubjectsSerializer(many=True)
    report_card = ReportCardSerializer(many=True)


    class Meta:
        model = Exams
        fields = ["id", "score","subject", "student", "report_card"]
        read_only_fields = ["id" ]
