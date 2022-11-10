from rest_framework import serializers
from .models import Student
from .models import Teacher
from addresses.serializers import AddressesSerializer
from addresses.models import Address
from grades.models import Grade
from report_cards.models import ReportCard
from django.core.mail import send_mail
from django.conf import settings
from utils.helpers import get_object_or_404_custom


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

        read_only_fields = ["id"]

        extra_kwargs = {"password": {"write_only": True}}

    def create(self, validated_data):
        address = validated_data.pop("address")
        grade_id = validated_data.pop("grade")

        grade = get_object_or_404_custom(
            Grade, "The especified Grade was not found!", id=grade_id
        )

        new_address = Address.objects.create(**address)

        new_student = Student.objects.create_user(
            **validated_data, address=new_address, grade=grade
        )

        if new_student:
            info = {
                "name": new_student.first_name + " " + new_student.last_name,
                "username": new_student.username,
                "password": validated_data["password"],
                "id": new_student.id,
            }

            send_mail(
                subject="Student registration was successful.",
                message="""                Hello {name}, this email is being sent as to inform you that your
                registration has been successful.

                Furthermore, you'll be able to login onto our system to check grades
                on our website at https://reinhardt-mgmt.herokuapp.com/api/login/,
                using the following credentials:
                check your email to access your account: https://reinhardt-mgmt.herokuapp.com/api/students/verify/{id}/

                    Username: {username}
                    Password: {password}""".format(
                    **info
                ),
                from_email=settings.EMAIL_HOST_USER,
                recipient_list=[new_student.email],
            )

        list_subjects = list(grade.subjects.all())

        for subject in list_subjects:
            ReportCard.objects.create(student=new_student, subject=subject)

        return new_student


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

        new_teacher = Teacher.objects.create_user(**validated_data, address=new_address)

        if new_teacher:
            info = {
                "name": new_teacher.first_name + " " + new_teacher.last_name,
                "username": new_teacher.username,
                "password": validated_data["password"],
                "id": new_teacher.id,
            }

            send_mail(
                subject="Teacher registration was successful.",
                message="""                Hello {name}, this email is being sent as to inform you that your
                    registration has been successful.

                    Furthermore, you'll be able to login onto our system on our website at
                    https://reinhardt-mgmt.herokuapp.com/api/login/, using the following
                    credentials:
                    check your email to access your account: https://reinhardt-mgmt.herokuapp.com/api/teachers/verify/{id}/

                        Username: {username}
                        Password: {password}""".format(
                    **info
                ),
                from_email=settings.EMAIL_HOST_USER,
                recipient_list=[new_teacher.email],
            )

        return new_teacher


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


class ReportStudentSerializer(serializers.ModelSerializer):
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

class StudentName(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = [
            "grade",
            "first_name",
            "last_name",
            "id",
        ]
