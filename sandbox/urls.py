from django.contrib import admin
from django.urls import path

from oscar.app import application

urlpatterns = [
    path('admin/', admin.site.urls),
    path(r'', application.urls),
]
