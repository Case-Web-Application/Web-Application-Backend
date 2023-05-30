from django.shortcuts import render
from .models import User


def home_page(request):
    users = User.objects.all()
    context = {'users': users}
    return render(request, 'home_page.html', context)

