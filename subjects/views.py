from .models import Subject
from .serializers import SubjectsSerializer, SubjectsPatchTeacherSerializer
from rest_framework.permissions import IsAdminUser
from rest_framework.authentication import TokenAuthentication
from rest_framework import generics

# Create your views here.


class SubjectView(generics.CreateAPIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAdminUser]

    serializer_class = SubjectsSerializer
    queryset = Subject.objects.all()


class SubjectsView(generics.ListAPIView):
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


class SubjectsDetailsTeacherView(generics.UpdateAPIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAdminUser]

    queryset = Subject.objects.all()
    serializer_class = SubjectsPatchTeacherSerializer
