from django.conf import settings
from django.conf.urls import i18n
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import include, path

from oscar.app import application

urlpatterns = [
    path('admin/', admin.site.urls),
    path('i18n/', include(i18n)),
    path('', application.urls),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
