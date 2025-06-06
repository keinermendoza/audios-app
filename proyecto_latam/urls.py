from django.contrib import admin
from django.urls import path, include
from django.conf import settings

urlpatterns = [
    path(settings.ADMIN_SITE_URL, admin.site.urls),
    path('', include('audios.urls')),
]
