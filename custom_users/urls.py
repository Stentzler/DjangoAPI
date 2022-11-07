from django.urls import path
from rest_framework.authtoken.views import ObtainAuthToken
from . import views

urlpatterns = [
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
    path("teachers/update/<str:id>/", views.UpdateTeacherView.as_view()),
    #
    path("students/exams/<str:student_id>/", views.GetStudentExams.as_view()),
]
