from django.urls import re_path
from oscar.core.loading import get_class

InvoicePreviewView = get_class("oscar_invoices.views", "InvoicePreviewView")


app_name = "oscar_invoices"
urlpatterns = [
    re_path(r"invoice/(?P<pk>\d+)/", InvoicePreviewView.as_view(), name="invoice"),
]
