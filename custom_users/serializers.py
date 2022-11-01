from rest_framework import serializers
from .models import Student
from .models import Teacher


class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model: Student

        field = "__all__"

        read_only_fields = ["id"]


class DetailedStudentSerializer(serializers.ModelSerializer):
    class Meta:
        model: Student

        field = "__all__"

        read_only_fields = ["id"]

    # adicionar address serializer
    # adicionar notas dos exames


###


class TeacherSerializer(serializers.ModelSerializer):
    class Meta:
        model: Teacher

        field = "__all__"

        read_only_fields = ["id"]


class DetailedTeacherSerializer(serializers.ModelSerializer):
    class Meta:
        model: Student

        field = "__all__"

        read_only_fields = ["id"]

    # adicionar address serializer
