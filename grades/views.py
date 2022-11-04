from django.shortcuts import render
from rest_framework import generics
from .models import Grade
from rest_framework.permissions import IsAdminUser
from .serializers import GradeSerializer, DetailedGradeSerializer
from subjects.serializers import SubjectsSerializer
# Create your views here.


class GradeView(generics.CreateAPIView):
    # permission_classes = [IsAdminUser]
    serializer_class = DetailedGradeSerializer
    queryset = Grade.objects.all()


class GradesView(generics.ListAPIView):
    # permission_classes = [IsAdminUser]
    serializer_class = GradeSerializer
    queryset = Grade.objects.all()


class GradesDetailsView(generics.RetrieveUpdateDestroyAPIView):
    # permission_classes = [IsAdminUser]
    serializer_class = GradeSerializer
    queryset = Grade.objects.all()
    lookup_url_kwarg = "id"
