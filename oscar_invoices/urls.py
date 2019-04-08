from django.urls import re_path

from . import views

app_name = "oscar_invoices"
urlpatterns = [
    re_path(r"invoice/(?P<pk>\d+)/", views.InvoicePreviewView.as_view(), name="invoice"),
]
