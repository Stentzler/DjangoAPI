from rest_framework import generics
# from rest_framework.authentication import TokenAuthentication
# from rest_framework.permissions import IsAdminUser
# from .permissions import IsAdminOrOwner
from exams.serializers import ExamsSerialzier
from exams.models import Exams



class ExamsCreateView(generics.CreateAPIView):
    # authentication_classes = [TokenAuthentication]
    # permission_classes = [IsAdminOrOwner]

    serializer_class = ExamsSerialzier


class ExamsListView(generics.ListAPIView):
    # authentication_classes = [TokenAuthentication]
    # permission_classes = [IsAdminUser]

    queryset = Exams.objects.all()
    serializer_class = ExamsSerialzier   


class UpdateExamsView(generics.UpdateAPIView):
    # authentication_classes = [TokenAuthentication]
    # permission_classes = [IsAdminOrOwner]

    queryset = Exams.objects.all()
    serializer_class = ExamsSerialzier
    lookup_url_kwarg = "id"    


class DeleteRetriveExamsView(generics.RetrieveDestroyAPIView):
    # authentication_classes = [TokenAuthentication]
    # permission_classes = [IsAdminOrOwner]
    
    queryset = Exams.objects.all()
    serializer_class = ExamsSerialzier
    lookup_url_kwarg = "id"    


