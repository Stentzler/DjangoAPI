from rest_framework import serializers
from .models import Student

class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = ["name","age","address","contacts","email","password","rg","is_teacher"]
        extra_kwargs = {'password': {'required': True,'write_only': True}}
        depth = 1