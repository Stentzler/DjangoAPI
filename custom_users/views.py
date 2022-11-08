from rest_framework.views import APIView, Request, Response, status
from rest_framework import generics
from django.shortcuts import get_object_or_404
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAdminUser
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
from django.shortcuts import get_object_or_404
from report_cards.serializers import ListReportCardSerializer
from exams.serializers import ExamsSerializer
import ipdb

## ---------------------- Student Views ----------------------
class StudentCreateView(generics.CreateAPIView):
    # authentication_classes = [TokenAuthentication]
    # permission_classes = [IsAdminUser]

    serializer_class = StudentSerializer


class StudentsListView(generics.ListAPIView):
    # authentication_classes = [TokenAuthentication]
    # permission_classes = [IsAdminUser]

    queryset = Student.objects.all()
    serializer_class = ListStudentSerializer


class DeleteRetriveStudentView(generics.RetrieveDestroyAPIView):
    # authentication_classes = [TokenAuthentication]
    # permission_classes = [IsAdminUser]

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
        reports = student.report_cards
        serializer = ListReportCardSerializer(reports, many=True)

        return Response(serializer.data, status.HTTP_200_OK)


class GetStudentExams(APIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsStudent]

    def get(self, request: Request) -> Response:
        student = get_object_or_404(Student, id=request.user.id)
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


## ------------------------- Teacher Views --------------------------:


class TeacherCreateView(generics.CreateAPIView):
    # authentication_classes = [TokenAuthentication]
    # permission_classes = [IsAdminUser]

    serializer_class = TeacherSerializer


class TeacherListView(generics.ListAPIView):
    # authentication_classes = [TokenAuthentication]
    # permission_classes = [IsAdminUser]

    queryset = Teacher.objects.all()
    serializer_class = ListTeacherSerializer


class DeleteRetriveTeacherView(generics.RetrieveDestroyAPIView):
    # authentication_classes = [TokenAuthentication]
    # permission_classes = [IsAdminUser]

    queryset = Teacher.objects.all()
    serializer_class = TeacherSerializer
    lookup_url_kwarg = "id"


class UpdateTeacherView(generics.UpdateAPIView):
    # authentication_classes = [TokenAuthentication]
    # permission_classes = [IsAdminUser]

    queryset = Teacher.objects.all()
    serializer_class = UpdateTeacherSerializer
    lookup_url_kwarg = "id"
