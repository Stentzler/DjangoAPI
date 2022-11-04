from django.urls import path
from . import views

urlpatterns = [
    path("register/subject/", views.SubjectView.as_view()),
    path("subjects/", views.SubjectsView.as_view()),
    path("subjects/<str:id>/", views.SubjectsDetailsView.as_view())

]
