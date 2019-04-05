from django.apps import AppConfig


class TestAppConfig(AppConfig):
    name = 'test_app'

    def ready(self):
        from . import receivers  # noqa isort:skip
