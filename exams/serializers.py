from rest_framework import serializers
from exams.models import Exams
from custom_users.serializers import StudentSerializer
from subjects.serializers import SubjectsSerializer


class ExamsSerialzier(serializers.ModelSerializer):
    student = StudentSerializer(many=True)
    subject = SubjectsSerializer(many=True)


    class Meta:
        model = Exams
        fields = ["id", "score","subject", "student"]
        read_only_fields = ["id" ]
