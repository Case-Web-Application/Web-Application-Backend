from django.contrib import admin
from django.urls import path, include
from .api import api
from testov import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/', api.urls),
    path('', views.home_page, name='home_page')
]
