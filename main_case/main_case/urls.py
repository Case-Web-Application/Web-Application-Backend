from django.contrib import admin
from django.urls import path, include
from .api import api
from testov.views import *
from main_case import settings
from django.conf.urls.static import static


urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/', api.urls),
    path('login/', login, name='login'),
    path('', index, name='index'),
    
]


if settings.DEBUG:
    urlpatterns += static(
        settings.MEDIA_URL,
        document_root=settings.MEDIA_ROOT)
