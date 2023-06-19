from django.shortcuts import render
from .models import User


def index(request):
    return render(request, 'index.html')

def login(request):
    return render(request, 'login.html')