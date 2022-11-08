from rest_framework import serializers
from exams.models import Exams
from grades.models import Grade
from custom_users.models import Student
import ipdb
from exams.exeptions import BadRequest

class ExamsSerializer(serializers.ModelSerializer):

    grades = serializers.UUIDField(write_only=True)

    class Meta:
        model = Exams
        fields = ["id", "score", "subject", "quarter", "grades"]
        read_only_fields = ["id"]
        extra_kwargs = {"grades": {"required": True}}

    def create(self, validated_data):
        subject = validated_data.pop("subject")
        grades = validated_data.pop("grades") 
        quarter = validated_data.pop("quarter")
        
        students = Student.objects.filter(grade_id=grades).all()
        """ grade=Grade.objects.filter(id=grades) """
        
        """ print(grade[0].subjects.all()) """
        
        #fazer verificação para retornar algo  caso a list_students venha vazio
        #caso contrario isso retornará erro 500
        
        if len(students)==0 :
            raise BadRequest({"message": "this class does not have any students yet, because of this exams cannot be created."})
        
        exams_list=[]
        for student in students:
            exams_created = Exams.objects.create(student=student,quarter=quarter,subject=subject)
            exams_list.append(exams_created)



        return exams_created
