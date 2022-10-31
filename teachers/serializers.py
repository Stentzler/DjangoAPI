from rest_framework import serializers
from .models import Teacher

class TeacherSerializer(serializers.ModelSerializer):
    class Meta:
        model= Teacher
        fields= ["name","age","address_id","contacts","email","password","is_teacher","cpf","rg"]
        extra_kwargs = {'password': {'required': True,'write_only': True}}