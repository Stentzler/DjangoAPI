from rest_framework import serializers
from custom_users.serializers import TeacherSerializer

from subjects.models import Subject
from custom_users.serializers import TeacherName


class SubjectsSerializer(serializers.ModelSerializer):
    id = serializers.CharField(read_only=True)

    class Meta:
        model = Subject
        fields = [
            "id",
            "name",
            "teacher",
        ]
