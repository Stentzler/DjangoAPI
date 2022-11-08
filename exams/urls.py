from django.urls import path
from . import views

urlpatterns = [
    path("register/exams/", views.ExamsCreateView.as_view()),
    path("exams/", views.ExamsListView.as_view()),
    path("exams/teacher/<str:exams_id>/", views.UpdateExamsView.as_view()),
    path("exams/<str:id>/", views.DeleteRetriveExamsView.as_view()),
    path("teacher/exams/", views.ListExamsByTeacher.as_view()),
]
