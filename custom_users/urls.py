from django.urls import path
from rest_framework.authtoken.views import ObtainAuthToken
from . import views

urlpatterns = [
    path("students/profile/", views.GetStudentProfile.as_view(), name="profile"),
    path("students/report_card/", views.GetStudentReports.as_view(), name="report"),
    path("students/exams/", views.GetStudentExams.as_view(), name="exams"),
    #
    path("login/", ObtainAuthToken.as_view()),
    #
    path("register/student/", views.StudentCreateView.as_view()),
    path("register/teacher/", views.TeacherCreateView.as_view()),
    #
    path("students/", views.StudentsListView.as_view()),
    path("teachers/", views.TeacherListView.as_view()),
    #
    path("students/<str:id>/", views.DeleteRetriveStudentView.as_view()),
    path("teachers/<str:id>/", views.DeleteRetriveTeacherView.as_view()),
    #
    path("students/update/<str:id>/", views.UpdateStudentView.as_view()),
    #
    path("teachers/update/<str:id>/", views.UpdateTeacherView.as_view()),
    path("users/update/address/<str:address_id>/", views.UserUpdateAddress.as_view()),
    #
    path("students/report_card/", views.GetStudentReports.as_view()),
    path("students/exams/", views.GetStudentExams.as_view()),
    #
    path("students/verify/<str:id>/", views.StudentsVerifyView.as_view()),
    path("teachers/verify/<str:id>/", views.TeacherVerifyView.as_view()),
    #
    path("teacher/profile/", views.TeacherListProfileView.as_view()),
    path("teacher/subjects/", views.TeacherListSubjectsView.as_view()),
]
