from django.http import HttpResponse
from django.contrib.auth.decorators import user_passes_test

from oscar.core.loading import get_model

from .utils import InvoiceCreator

Invoice = get_model('oscar_invoices', 'Invoice')


@user_passes_test(lambda user: user.is_superuser)
def invoice(request, pk):
    iv = Invoice.objects.get(pk=pk)
    ic = InvoiceCreator()
    rendered_template = ic.render_document(
        iv,
        legal_entity=iv.legal_entity,
        order=iv.order,
        use_path=False,
    )
    return HttpResponse(rendered_template)
