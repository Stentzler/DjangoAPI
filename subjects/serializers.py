from rest_framework import serializers
from custom_users.serializers import TeacherSerializer

from subjects.models import Subject


class SubjectsSerializer(serializers.ModelSerializer):
    id = serializers.CharField(read_only=True)

    class Meta:
        model = Subject
        fields = [
            'id', 
            'name',
            'teacher',
        ]
        teacher = TeacherSerializer(read_only=True)