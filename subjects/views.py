from django.shortcuts import render
from .models import Subject
from .serializers import SubjectsSerializer,SubjectsPatchTeacherSerializer
from rest_framework import generics
# Create your views here.


class SubjectView(generics.CreateAPIView):
    # permission_classes = [IsAdminUser]
    serializer_class = SubjectsSerializer
    queryset = Subject.objects.all()


class SubjectsView(generics.ListAPIView):
    # permission_classes = [IsAdminUser]
    serializer_class = SubjectsSerializer
    queryset = Subject.objects.all()

class SubjectsDetailsView(generics.RetrieveUpdateDestroyAPIView):
    # permission_classes = [IsAdminUser]
    serializer_class = SubjectsSerializer
    queryset = Subject.objects.all()
    lookup_url_kwarg = "id"

class SubjectsDetailsTeacherView(generics.UpdateAPIView):
    # permission_classes = [IsAdminUser]
    queryset = Subject.objects.all()
    serializer_class = SubjectsPatchTeacherSerializer