from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse

def index(request):
    return render(request, "index/index.html")

def contact(request):
    return render(request, "index/contact.html")

def about(request):
    return render(request, "index/about.html")