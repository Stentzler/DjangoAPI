from rest_framework import serializers

from report_cards.models import ReportCard

class ReportCardSerializer(serializers.ModelSerializer):
    id = serializers.CharField(read_only=True)

    average = serializers.SerializerMethodField()

    class Meta:
        model = ReportCard
        fields = [
            'id',
            'student'
            'subject'
            'result_q1',
            'result_q2',
            'result_q3',
            'result_q4',
            'average',
            'attendance',
            'is_approved',
            'is_active',
        ]
        depth = 1

    def get_average(self, obj):
        return (obj.N1 + obj.N2 + obj.N3 + obj.N4) / 4