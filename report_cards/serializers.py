from rest_framework import serializers

from report_cards.models import ReportCard

class ReportCardSerializer(serializers.ModelSerializer):
    id = serializers.CharField(read_only=True)

    class Meta:
        model = ReportCard
        fields = [
            'id',
            'student'
            'N1',
            'N2',
            'N3',
            'N4',
            'average',
            'attendance',
            'is_approved',
            'is_active',
        ]
        depth = 1