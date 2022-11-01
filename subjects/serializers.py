from rest_framework import serializers

from subjects.models import Subject


class SubjectsSerializer(serializers.ModelSerializer):
    id = serializers.CharField(read_only=True)

    class Meta:
        model = Subject
        fields = [
            'id', 
            'name',
            'teacher',
        ]
        # teacher = (read_only=True)