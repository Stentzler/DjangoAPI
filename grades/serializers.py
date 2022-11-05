from rest_framework import serializers
from subjects.serializers import SubjectsSerializer
from .models import Grade
from subjects.serializers import SubjectsSerializer
from subjects.models import Subject
from django.shortcuts import get_object_or_404
# import ipdb 
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
