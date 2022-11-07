from rest_framework import serializers

from report_cards.models import ReportCard
from custom_users.serializers import ListStudentSerializer


class ReportCardSerializer(serializers.ModelSerializer):
    id = serializers.CharField(read_only=True)

    average = serializers.SerializerMethodField()

    class Meta:
        model = ReportCard
        fields = [
            "id",
            "student", 
            "subject",
            "result_q1",
            "result_q2",
            "result_q3",
            "result_q4",
            "average",
            "attendance",
            "is_approved",
            "is_active",
        ]
        depth = 1

    def get_average(self, obj):
        return (obj.result_1 + obj.result_2 + obj.result_3 + obj.result_4) / 4


class ListReportCardSerializer(serializers.ModelSerializer):
    student = ListStudentSerializer(many=False)

    class Meta:
        model = ReportCard
        fields = "__all__"
        depth = 1
