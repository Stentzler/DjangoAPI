from rest_framework import generics
from custom_users.models import Teacher
from rest_framework.authentication import TokenAuthentication
from django_filters import rest_framework as filters
# from rest_framework.permissions import IsAdminUser
from .permissions import IsAdminOrOwner, IsTeacher
from exams.serializers import ExamsSerializer
from exams.models import Exams


class ListExamsByTeacher(generics.ListAPIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsTeacher]
    filter_backends = (filters.DjangoFilterBackend,)
    filterset_fields = (
        "subject",
        "quarter",
        "student",
    )

    serializer_class = ExamsSerializer

    def get_queryset(self):
        teacher = self.request.user
        exams_from_teacher = Exams.objects.filter(subject__teacher=teacher)

        return exams_from_teacher


class ExamsCreateView(generics.CreateAPIView):
    # authentication_classes = [TokenAuthentication]
    # permission_classes = [IsAdminOrOwner]

    serializer_class = ExamsSerializer


class ExamsListView(generics.ListAPIView):
    # authentication_classes = [TokenAuthentication]
    # permission_classes = [IsAdminUser]

    queryset = Exams.objects.all()
    serializer_class = ExamsSerializer


class UpdateExamsView(generics.UpdateAPIView):
    # authentication_classes = [TokenAuthentication]
    # permission_classes = [IsAdminOrOwner]

    queryset = Exams.objects.all()
    serializer_class = ExamsSerializer
    lookup_url_kwarg = "id"


class DeleteRetriveExamsView(generics.RetrieveDestroyAPIView):
    # authentication_classes = [TokenAuthentication]
    # permission_classes = [IsAdminOrOwner]

    queryset = Exams.objects.all()
    serializer_class = ExamsSerializer
    lookup_url_kwarg = "id"
