from django.urls import path
from . import views

urlpatterns = [
    path("register/grade/", views.GradeView.as_view()),
    path("grades/", views.GradesView.as_view()),
    path("grades/<str:id>/", views.GradesDetailsView.as_view()),
]
