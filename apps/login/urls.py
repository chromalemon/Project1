from django.urls import path
from . import views

urlpatterns = [
    path("", views.login, name="login"),
    path("student/", views.student, name="student-login"),
    path("staff/", views.staff, name="staff-login"),
]
