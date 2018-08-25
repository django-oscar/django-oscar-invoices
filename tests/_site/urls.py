from django.conf.urls import path, include
from django.conf.urls import i18n
from django.contrib import admin
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

from oscar.app import application

admin.autodiscover()

urlpatterns = [
    path('admin/', admin.site.urls),
    path('i18n/', include(i18n)),
    path('', application.urls),
]

urlpatterns += staticfiles_urlpatterns()
