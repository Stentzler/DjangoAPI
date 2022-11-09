from django.urls import path
from . import views

urlpatterns = [
    path("absence/<str:student_id>/", views.AddAbsenceView().as_view()),
]