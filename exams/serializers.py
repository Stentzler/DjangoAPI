from rest_framework import serializers
from exams.models import Exams
from grades.models import Grade
from custom_users.models import Student
import ipdb
from exams.exeptions import BadRequest,Unauthorized

class ExamsSerializer(serializers.ModelSerializer):

    grades = serializers.UUIDField(write_only=True)

    class Meta:
        model = Exams
        fields = ["id", "score", "description","data","subject", "quarter", "grades"]
        read_only_fields = ["id"]
        extra_kwargs = {"grades": {"required": True}}

    def create(self, validated_data):
        subject = validated_data.pop("subject")
        description=validated_data.pop("description")
        data=validated_data.pop("data")
        grades = validated_data.pop("grades") 
        quarter = validated_data.pop("quarter")
        
        students = Student.objects.filter(grade_id=grades).all()
        grade=Grade.objects.filter(id=grades) 
        grades_subjects=list(grade[0].subjects.all())
       
        
        if len(students) == 0:
            raise BadRequest({"message": "Class has no students registered; no exams could be created."})
        
        for subjects in grades_subjects:
            if subject.id == subjects.id:
                for student in students:
                    exams_created = Exams.objects.create(student=student,quarter=quarter,subject=subject,description=description,data=data)
                return exams_created
            else:
                raise Unauthorized({"message": "This subject does not belong to this grades."})

