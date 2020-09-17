from django.apps import apps
from django.conf.urls import i18n
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.urls import include, path


urlpatterns = [
    path('i18n/', include(i18n)),
    path('', include(apps.get_app_config('oscar').urls[0])),
]

urlpatterns += staticfiles_urlpatterns()
