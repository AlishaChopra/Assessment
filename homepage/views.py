from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from django.contrib.auth.models import User


# Create your views here.


def home(request):
    return render(request, 'homepage/home.html')

def about(request):
    return render(request, 'homepage/about.html', {'title': 'About'})
