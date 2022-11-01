from rest_framework import serializers
# from subjects.serializers import SubjectSerializer ------------- Ainda nao existe
from .models import Grade


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

    # subjects = SubjectSerializer( ------------------ Ainda nao existe
    #     many=True,
    # )
