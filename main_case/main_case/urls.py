from django.contrib import admin
from django.urls import path, include
from .api import api
from testov import views
from main_case import settings
from django.conf.urls.static import static


urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/', api.urls),
    path('', views.index, name='index'),
]


if settings.DEBUG:
    urlpatterns += static(
        settings.MEDIA_URL,
        document_root=settings.MEDIA_ROOT)
