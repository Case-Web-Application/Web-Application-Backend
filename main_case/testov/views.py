from django.shortcuts import render
from .models import User


def index(request):
    return render(request, 'index.html')

