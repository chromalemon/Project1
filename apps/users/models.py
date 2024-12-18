from django.db import models
from django.contrib.auth.models import AbstractUser, AbstractBaseUser, BaseUserManager
from django.utils.translation import gettext_lazy as _

class CustomUser(AbstractUser):
    subjects_choices = {
        "MA": "Mathematics",
        "FM": "Further Mathematics",
        "CS": "Computer Science",
        "PH": "Physics",
    }
    subjects = models.CharField(max_length=128, choices=subjects_choices)
    school = models.CharField(_("school name"),max_length=128)


class Classroom(models.Model):
    room_num = models.IntegerField(default=0)
    seats_num = models.IntegerField(default=0)
    room_type = models.CharField(max_length=64)
    teacher_users = models.ManyToManyField(CustomUser, related_name="teacher_users")
    student_users = models.ManyToManyField(CustomUser, related_name="student_users")
    available = models.BooleanField(blank=True)

class Teacher(CustomUser):
    authority_choices = {
        1: "Teacher",
        2: "Deputy Head",
        3: "Head",
    }
    authority = models.IntegerField(default=1, choices=authority_choices)
    main_class = models.IntegerField(default=None, blank=True)

class Student(CustomUser):
    entry_year = models.IntegerField(default=None)
    prefect_status = models.BooleanField(default=False)
