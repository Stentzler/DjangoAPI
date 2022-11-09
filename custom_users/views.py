from rest_framework.views import APIView, Request, Response, status
from rest_framework import generics
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAdminUser
from .permissions import StudentIsAdminPermission
from exams.permissions import IsTeacher
from custom_users.serializers import (
    StudentSerializer,
    TeacherSerializer,
    ListStudentSerializer,
    ListTeacherSerializer,
    UpdateStudentSerializer,
    UpdateTeacherSerializer,
)
from custom_users.models import Student, Teacher
from exams.permissions import IsStudent
from subjects.models import Subject
from subjects.serializers import SubjectsSerializer
from exams.models import Exams
from django.shortcuts import get_object_or_404, get_list_or_404
from report_cards.serializers import ListReportCardSerializer
from exams.serializers import ExamsSerializer
import ipdb

# ---------------------- Student Views ----------------------


class StudentCreateView(generics.CreateAPIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAdminUser]

    serializer_class = StudentSerializer


class StudentsListView(generics.ListAPIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAdminUser]

    queryset = Student.objects.all()
    serializer_class = ListStudentSerializer


class DeleteRetriveStudentView(generics.RetrieveDestroyAPIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAdminUser]

    queryset = Student.objects.all()
    serializer_class = StudentSerializer
    lookup_url_kwarg = "id"


class UpdateStudentView(generics.UpdateAPIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAdminUser]

    queryset = Student.objects.all()
    serializer_class = UpdateStudentSerializer
    lookup_url_kwarg = "id"


class GetStudentReports(APIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsStudent]

    def get(self, request: Request) -> Response:
        student = get_object_or_404(Student, id=request.user.id)
        self.check_object_permissions(request=request, obj=student.id)
        reports = student.report_cards
        serializer = ListReportCardSerializer(reports, many=True)

        return Response(serializer.data, status.HTTP_200_OK)


class GetStudentExams(APIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsStudent]

    def get(self, request: Request) -> Response:
        student = get_object_or_404(Student, id=request.user.id)
        self.check_object_permissions(request=request, obj=student.id)
        exams = student.exams
        serializer = ExamsSerializer(exams, many=True)

        return Response(serializer.data, status.HTTP_200_OK)


class GetStudentProfile(APIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsStudent]

    def get(self, request: Request) -> Response:

        student = get_object_or_404(Student, id=request.user.id)

        serializer = StudentSerializer(student)

        return Response(serializer.data, status.HTTP_200_OK)


class StudentsVerifyView(APIView):
    def get(self, request: Request, id: str) -> Response:
        students = Student.objects.get(id=id)
        if students.is_active == True:
            return Response(
                {"msg": "your email has already been verified"},
                status.HTTP_400_BAD_REQUEST,
            )
        students.is_active = True
        students.save()
        return Response(
            {"msg": "email successfully verified, your account is ready to use"},
            status.HTTP_200_OK,
        )


# ------------------------- Teacher Views --------------------------:


class TeacherCreateView(generics.CreateAPIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAdminUser]

    serializer_class = TeacherSerializer


class TeacherListView(generics.ListAPIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAdminUser]

    queryset = Teacher.objects.all()
    serializer_class = ListTeacherSerializer


class TeacherListProfileView(APIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsTeacher]

    def get(self, request: Request) -> Response:

        teacher = get_object_or_404(Teacher, id=request.user.id)
        serializer = TeacherSerializer(teacher)
        return Response(serializer.data, status.HTTP_200_OK)


class TeacherListSubjectsView(APIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsTeacher]

    def get(self, request: Request) -> Response:

        teacher = get_object_or_404(Teacher, id=request.user.id)
        serializer = TeacherSerializer(teacher)
        teacher_id = serializer.data["id"]
        teacher_subject = get_list_or_404(Subject, teacher_id=teacher_id)
        subject_serializer = SubjectsSerializer(teacher_subject, many=True)

        return Response(subject_serializer.data, status.HTTP_200_OK)


class DeleteRetriveTeacherView(generics.RetrieveDestroyAPIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAdminUser]

    queryset = Teacher.objects.all()
    serializer_class = TeacherSerializer
    lookup_url_kwarg = "id"


class UpdateTeacherView(generics.UpdateAPIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAdminUser]

    queryset = Teacher.objects.all()
    serializer_class = UpdateTeacherSerializer
    lookup_url_kwarg = "id"


class TeacherVerifyView(APIView):
    def get(self, request: Request, id: str) -> Response:
        teacher = Teacher.objects.get(id=id)
        if teacher.is_active == True:
            return Response(
                {"msg": "your email has already been verified"},
                status.HTTP_400_BAD_REQUEST,
            )
        teacher.is_active = True
        teacher.save()
        return Response(
            {"msg": "email successfully verified, your account is ready to use"},
            status.HTTP_200_OK,
        )
