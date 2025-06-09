from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path(settings.ADMIN_SITE_URL, admin.site.urls),
    path('', include('audios.urls', namespace="audios")),
    path('auth/', include('custom_auth.urls', namespace="custom_auth")),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)