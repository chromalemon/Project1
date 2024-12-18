from django.db import models
from django.contrib.auth.models import AbstractUser, AbstractBaseUser, BaseUserManager
from django.utils.translation import gettext_lazy as _

class CustomUser():
    school = models.CharField(_("school name"),max_length=128)


class TeacherUser(CustomUser):
    pass

class StudentUser(CustomUser):
    pass 