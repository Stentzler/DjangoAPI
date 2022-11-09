from rest_framework import generics
from .models import Grade
from rest_framework.permissions import IsAdminUser
from rest_framework.authentication import TokenAuthentication
from .serializers import GradeSerializer, DetailedGradeSerializer

class GradeView(generics.CreateAPIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAdminUser]

    serializer_class = DetailedGradeSerializer
    queryset = Grade.objects.all()


class GradesView(generics.ListAPIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAdminUser]

    serializer_class = GradeSerializer
    queryset = Grade.objects.all()


class GradesDetailsView(generics.RetrieveUpdateDestroyAPIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAdminUser]

    serializer_class = GradeSerializer
    queryset = Grade.objects.all()
    lookup_url_kwarg = "id"
