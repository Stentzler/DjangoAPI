from rest_framework import serializers
from report_cards.models import ReportCard
from exams.models import Exams
from custom_users.models import Student


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
        return (obj.result_q1 + obj.result_q2 + obj.result_q3 + obj.result_q4) / 4


#####
class ListStudentReportSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = [
            "grade",
            "first_name",
            "last_name",
        ]


####
class ListReportCardSerializer(serializers.ModelSerializer):
    student = ListStudentReportSerializer(many=False)

    result_q1 = serializers.SerializerMethodField()
    result_q2 = serializers.SerializerMethodField()
    result_q3 = serializers.SerializerMethodField()
    result_q4 = serializers.SerializerMethodField()
    average = serializers.SerializerMethodField()
    is_approved = serializers.SerializerMethodField()
    attendance = serializers.SerializerMethodField()

    class Meta:
        model = ReportCard
        fields = "__all__"
        depth = 1

    #

    def calc_total(self, exams, stu_id, sub_id):
        total_score = 0
        total_exams = 0

        for exam in exams:
            if exam.student.id == stu_id and exam.subject.id == sub_id:
                total_score += exam.score
                total_exams += 1

        if total_exams > 0:
            return round(total_score / total_exams, 2)

        return "Nenhuma nota neste quarter"

    #

    def get_result_q1(self, obj):
        student_id = obj.student.id
        subject_id = obj.subject.id
        q1_exams = Exams.objects.all().filter(quarter="q1")

        return self.calc_total(q1_exams, student_id, subject_id)

    #

    def get_result_q2(self, obj):
        student_id = obj.student.id
        subject_id = obj.subject.id
        q2_exams = Exams.objects.all().filter(quarter="q2")

        return self.calc_total(q2_exams, student_id, subject_id)

    #

    def get_result_q3(self, obj):
        student_id = obj.student.id
        subject_id = obj.subject.id
        q3_exams = Exams.objects.all().filter(quarter="q3")

        return self.calc_total(q3_exams, student_id, subject_id)

    #

    def get_result_q4(self, obj):
        student_id = obj.student.id
        subject_id = obj.subject.id
        q4_exams = Exams.objects.all().filter(quarter="q4")

        return self.calc_total(q4_exams, student_id, subject_id)

    #

    def get_average(self, obj):
        if (
            isinstance(self.get_result_q1(obj), str)
            or isinstance(self.get_result_q2(obj), str)
            or isinstance(self.get_result_q3(obj), str)
            or isinstance(self.get_result_q4(obj), str)
        ):
            return "Média final ainda não disponível"

        return round(
            (
                self.get_result_q1(obj)
                + self.get_result_q2(obj)
                + self.get_result_q3(obj)
                + self.get_result_q4(obj)
            )
            / 4,
            2,
        )

    def get_is_approved(self, obj):
        if isinstance(self.get_average(obj), float | int):
            if self.get_average(obj) >= 60:
                return True
            else:
                return False
        else:
            return False

    def get_attendance(self, obj):
        single_class_value = round(100 / obj.subject.total_classes, 2)

        if (100 - single_class_value * obj.absences) < 0:
            return 0
        else:
            return 100 - single_class_value * obj.absences


class AbsenceReportCardSerializer(serializers.Serializer):
    subject = serializers.CharField()
    absences = serializers.IntegerField()
