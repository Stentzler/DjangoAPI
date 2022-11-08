from rest_framework import generics
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAdminUser
from .permissions import TeacherIsAdminPermission
from exams.serializers import ExamsSerializer
from exams.models import Exams




class ExamsListView(generics.ListAPIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAdminUser]

    queryset = Exams.objects.all()
    serializer_class = ExamsSerializer   


class UpdateExamsView(generics.UpdateAPIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [TeacherIsAdminPermission]

    queryset = Exams.objects.all()
    serializer_class = ExamsSerializer
    lookup_url_kwarg = "exams_id"  



class DeleteRetriveExamsView(generics.RetrieveDestroyAPIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAdminUser]
    
    queryset = Exams.objects.all()
    serializer_class = ExamsSerializer
    lookup_url_kwarg = "id"    


