from django.shortcuts import render, redirect
from django.contrib import messages 
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from apps.users.models import *
from django.http import HttpResponse

# Create your views here.

def login(request):
    if request.method == "POST":
        email = request.POST.get("email")
        password = request.POST.get("password")

    return render(request, "login/login.html")

def student(request):
    return render(request, "login/student-login.html")

def staff(request):
    return render(request, "login/staff-login.html")
