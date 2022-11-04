from rest_framework import serializers
from .models import Student
from .models import Teacher
from addresses.serializers import AddressesSerializer
from addresses.models import Address
from grades.models import Grade
from django.shortcuts import get_object_or_404


class StudentSerializer(serializers.ModelSerializer):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields["password"].required = True
        self.fields["first_name"].required = True
        self.fields["last_name"].required = True

    address = AddressesSerializer(many=False)
    grade = serializers.UUIDField()

    class Meta:
        model = Student
        fields = [
            "address",
            "grade",
            "username",
            "first_name",
            "last_name",
            "rg",
            "age",
            "email",
            "password",
            "contacts",
            "id",
        ]

        read_only_fields = [
            "id",
        ]

        extra_kwargs = {"password": {"write_only": True}}

    def create(self, validated_data):
        address = validated_data.pop("address")
        grade_id = validated_data.pop("grade")

        grade = get_object_or_404(Grade, id=grade_id)

        new_address = Address.objects.create(**address)

        return Student.objects.create_user(
            **validated_data, address=new_address, grade=grade
        )


class TeacherSerializer(serializers.ModelSerializer):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields["password"].required = True
        self.fields["first_name"].required = True
        self.fields["last_name"].required = True

    address = AddressesSerializer(many=False)

    class Meta:
        model = Teacher

        fields = [
            "address",
            "cpf",
            "username",
            "first_name",
            "last_name",
            "rg",
            "age",
            "email",
            "password",
            "contacts",
            "id",
        ]

        read_only_fields = ["id"]

        extra_kwargs = {"password": {"write_only": True}}

    def create(self, validated_data):
        address = validated_data.pop("address")

        new_address = Address.objects.create(**address)

        return Teacher.objects.create_user(**validated_data, address=new_address)


class ListStudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = [
            "address",
            "grade",
            "username",
            "first_name",
            "last_name",
            "rg",
            "age",
            "email",
            "contacts",
            "id",
        ]


class ListTeacherSerializer(serializers.ModelSerializer):
    class Meta:
        model = Teacher

        fields = [
            "address",
            "cpf",
            "username",
            "first_name",
            "last_name",
            "rg",
            "age",
            "email",
            "contacts",
            "id",
        ]


class UpdateStudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = [
            "username",
            "first_name",
            "last_name",
            "rg",
            "age",
            "email",
            "contacts",
            "id",
        ]

        read_only_fields = ["id"]


class UpdateTeacherSerializer(serializers.ModelSerializer):
    class Meta:
        model = Teacher
        fields = [
            "username",
            "first_name",
            "last_name",
            "rg",
            "cpf",
            "age",
            "email",
            "contacts",
            "id",
        ]

        read_only_fields = ["id"]


class TeacherName(serializers.ModelSerializer):
    class Meta:
        model = Teacher
        fields = [
            "first_name",
            "last_name",
            "id",
        ]

        read_only_fields = ["id"]
