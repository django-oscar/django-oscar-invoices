from django.urls import re_path
from django.utils.translation import gettext_lazy as _
from oscar.core.application import OscarConfig


class InvoicesConfig(OscarConfig):
    label = 'oscar_invoices'
    name = 'oscar_invoices'
    verbose_name = _('Invoices')

    default_permissions = ["is_staff"]

    default = True

    def ready(self):
        from . import views
        self.invoice_view = views.InvoicePreviewView

    def get_urls(self):
        urlpatterns = [
            re_path(r"invoice/(?P<pk>\d+)/", self.invoice_view.as_view(),
                    name="invoice"),
        ]
        return self.post_process_urls(urlpatterns)
