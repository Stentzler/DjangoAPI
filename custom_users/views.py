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
from subjects.models import Subject
from subjects.serializers import SubjectsSerializer
from exams.models import Exams
from django.shortcuts import get_object_or_404, get_list_or_404
from report_cards.serializers import ListReportCardSerializer
from exams.serializers import ExamsSerializer
import ipdb

## ---------------------- Student Views ----------------------
class StudentCreateView(generics.CreateAPIView):
    serializer_class = StudentSerializer


class StudentsListView(generics.ListAPIView):
    queryset = Student.objects.all()
    serializer_class = ListStudentSerializer


class DeleteRetriveStudentView(generics.RetrieveDestroyAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
    lookup_url_kwarg = "id"


class UpdateStudentView(generics.UpdateAPIView):
    queryset = Student.objects.all()
    serializer_class = UpdateStudentSerializer
    lookup_url_kwarg = "id"


class GetStudentReports(APIView):
    def get(self, request: Request, student_id: str) -> Response:
        student = get_object_or_404(Student, id=student_id)
        reports = student.report_cards
        serializer = ListReportCardSerializer(reports, many=True)

        return Response(serializer.data, status.HTTP_200_OK)
        
class GetStudentExams(APIView):
    def get(self, request: Request, student_id: str) -> Response:
        student = get_object_or_404(Student, id=student_id)
        exams = student.exams

        serializer = ExamsSerializer(exams, many=True)

        return Response(serializer.data, status.HTTP_200_OK)


## ------------------------- Teacher Views --------------------------:


class TeacherCreateView(generics.CreateAPIView):
    serializer_class = TeacherSerializer


class TeacherListView(generics.ListAPIView):
    queryset = Teacher.objects.all()
    serializer_class = ListTeacherSerializer
    
class TeacherListProfileView(APIView):
    authentication_classes=[TokenAuthentication]
    def get(self, request: Request) -> Response:
        
        
        teacher = get_object_or_404(Teacher, id=request.user.id)
        serializer = TeacherSerializer(teacher)
        return Response(serializer.data, status.HTTP_200_OK)
 
class TeacherListSubjectsView(APIView):
    authentication_classes=[TokenAuthentication]
    def get(self, request: Request) -> Response:
        
        
        teacher = get_object_or_404(Teacher, id=request.user.id)
        serializer = TeacherSerializer(teacher)
        teacher_id=serializer.data["id"]
        teacher_subject=get_list_or_404(Subject,teacher_id=teacher_id)
        subejct_serializer= SubjectsSerializer(teacher_subject,many=True)
        print(teacher_subject)
       
        return Response(subejct_serializer.data, status.HTTP_200_OK)    
    
        


class DeleteRetriveTeacherView(generics.RetrieveDestroyAPIView):
    queryset = Teacher.objects.all()
    serializer_class = TeacherSerializer
    lookup_url_kwarg = "id"


class UpdateTeacherView(generics.UpdateAPIView):
    queryset = Teacher.objects.all()
    serializer_class = UpdateTeacherSerializer
    lookup_url_kwarg = "id"



