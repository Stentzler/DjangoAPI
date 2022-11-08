from rest_framework import serializers
from exams.models import Exams
from custom_users.models import Student

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
        
        for student in students:
            exams_created = Exams.objects.create(student=student,quarter=quarter,subject=subject)

        return exams_created
