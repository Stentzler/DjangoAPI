from curses import meta
from rest_framework import serializers
from exams.models import Exams
from report_cards.models import ReportCard
from students.serializer import StudentSerializer
from subjects.serializer import SubjectsSerializer


class ExamsSerialzier(serializers.ModelSerializer):
    student = StudentSerializer(many=True)
    subject = SubjectsSerializer(many=True)
    report_card = ReportCard(many=True)

    class Meta:
        model = Exams
        fields = ["id", "score", "subject", "student", "report_card"]
        read_only_fields = ["id"]
