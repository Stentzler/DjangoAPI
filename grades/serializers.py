from rest_framework import serializers
from subjects.serializers import SubjectsSerializer
from .models import Grade
from subjects.serializers import SubjectsSerializer


class GradeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Grade
        fields = "__all__"

        read_only_fields = ["id"]


class DetailedGradeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Grade
        fields = "__all__"

        read_only_fields = ["id"]

        subjects = SubjectsSerializer(
            many=True,
        )
