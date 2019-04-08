from oscar.core.loading import get_model
from django.contrib.auth.mixins import UserPassesTestMixin
from django.http import HttpResponse
from django.views.generic import View
from django.views.generic.detail import SingleObjectMixin

from .utils import InvoiceCreator

Invoice = get_model('oscar_invoices', 'Invoice')


class InvoicePreviewView(UserPassesTestMixin, SingleObjectMixin, View):
    queryset = Invoice.objects.all()

    def test_func(self):
        user = self.request.user
        return user.is_staff

    def get(self, request, *args, **kwargs):
        invoice = self.get_object()
        rendered_invoice = InvoiceCreator().render_document(
            invoice=invoice,
            legal_entity=invoice.legal_entity,
            order=invoice.order,
            use_path=False,
        )
        return HttpResponse(rendered_invoice)
