from django.shortcuts import render
from .models import Subject
from .serializers import SubjectsSerializer, SubjectsPatchTeacherSerializer
from rest_framework.permissions import IsAdminUser
from rest_framework.authentication import TokenAuthentication
from rest_framework import generics

# Create your views here.


class SubjectView(generics.ListCreateAPIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAdminUser]

    serializer_class = SubjectsSerializer
    queryset = Subject.objects.all()


class SubjectsDetailsView(generics.RetrieveUpdateDestroyAPIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAdminUser]

    serializer_class = SubjectsSerializer
    queryset = Subject.objects.all()
    lookup_url_kwarg = "id"
