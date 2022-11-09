from exams.permissions import IsTeacherOrAdmin
from rest_framework.authentication import TokenAuthentication
from rest_framework import generics
from rest_framework.views import Response, status
from report_cards.serializers import (
    AbsenceReportCardSerializer,
    ListReportCardSerializer,
)
from report_cards.models import ReportCard
from custom_users.models import Student, Teacher
from subjects.models import Subject
from django.core.mail import send_mail
from django.conf import settings
from utils.helpers import get_object_or_404_custom


class AddAbsenceView(generics.UpdateAPIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsTeacherOrAdmin]

    serializer_class = AbsenceReportCardSerializer
    queryset = ReportCard.objects.all()

    def update(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data, partial=False)
        serializer.is_valid(raise_exception=True)

        student_id = self.kwargs.pop("student_id")
        subject_id = request.data.pop("subject")

        student = get_object_or_404_custom(
            Student, "Provided student was not found", id=student_id
        )
        subject = get_object_or_404_custom(
            Subject, "Provided student was not found", id=subject_id
        )

        if request.user.role == "TEACHER":
            teacher = Teacher.objects.get(id=request.user.id)
            if subject not in teacher.Subjects.all():
                return Response(
                    {"detail": "Subject does not belong to this teacher"},
                    status.HTTP_403_FORBIDDEN,
                )

        report_card = get_object_or_404_custom(
            ReportCard,
            "Provided report_card was not found",
            student=student,
            subject=subject,
        )

        report_card.absences = report_card.absences + request.data["absences"]
        if report_card.absences > subject.total_classes:
            report_card.absences = subject.total_classes
        report_card.save()

        updated_report_card = ListReportCardSerializer(report_card)

        if updated_report_card.data["attendance"] < 85:
            send_mail(
                subject="Student attendance grade is under 85%",
                message=f"""                Hello {student.first_name} {student.last_name},
                we would like to inform you that your current attendance grade is {updated_report_card.data['attendance']},
                for the subject {subject.name}, at the count of {updated_report_card.data['absences']} absences 
                as of today, out of {subject.total_classes} total classes.
                
                If you think there were any absences that were mistakenly applied, 
                contact the student support. This is an automated email, do 
                not reply.""",
                from_email=settings.EMAIL_HOST_USER,
                recipient_list=[student.email],
            )

        return Response(
            {
                "detail": f"Absences registered successfully. Total student absences: {report_card.absences}"
            },
            status.HTTP_200_OK,
        )
