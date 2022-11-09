from rest_framework import serializers
from subjects.exceptions import NonUpdatableKeyError
from subjects.models import Subject


class SubjectsSerializer(serializers.ModelSerializer):
    id = serializers.CharField(read_only=True)

    class Meta:
        model = Subject
        fields = ["id", "name", "teacher", "total_classes"]


class SubjectsPatchTeacherSerializer(serializers.ModelSerializer):
    id = serializers.CharField(read_only=True)

    class Meta:
        model = Subject
        fields = ["id", "name", "teacher", "total_classes"]

    def update(self, instance, validated_data):

        for key, value in validated_data.items():
            if key == "name":
                raise NonUpdatableKeyError(
                    {"name": "You can not update name property in this route."}
                )

            setattr(instance, key, value)

        instance.save()
        return instance
