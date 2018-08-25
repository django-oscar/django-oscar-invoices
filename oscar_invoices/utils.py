from django.core.files.base import ContentFile
from django.template.loader import render_to_string

from oscar.core.loading import get_model

from . import app_settings

LegalEntity = get_model('oscar_invoices', 'LegalEntity')


class InvoiceCreator(object):
    _invoice_model = None

    def get_legal_entity(self):
        return LegalEntity.objects.first()

    def get_invoice_model(self):
        if not self._invoice_model:
            app_label, model_name = app_settings.OSCAR_INVOICES_INVOICE_MODEL.split('.')
            self._invoice_model = get_model(app_label, model_name)
        return self._invoice_model

    def get_invoice_filename(self, invoice):
        return 'invoice_{}.html'.format(invoice.order.number)

    def generate_invoice_number(self, **kwargs):
        Invoice = self.get_invoice_model()
        pk = Invoice.get_last_pk() + 1
        return '%06d' % pk

    def get_invoice_template_context(self, invoice, **kwargs):
        order = kwargs.pop('order', None)
        legal_entity = kwargs.pop('legal_entity', None)
        template_context = {
            'invoice': invoice,
            'order': order,
            'legal_entity': legal_entity,
            'legal_entity_address': legal_entity.addresses.first(),
        }
        template_context.update(**kwargs)
        return template_context

    def render_document(self, invoice, **kwargs):
        """
        Return rendered from html template invoice document.
        """
        template_name = 'oscar_invoices/invoice.html'
        template_context = self.get_invoice_template_context(invoice, **kwargs)
        return render_to_string(template_name, template_context)

    def generate_document(self, invoice, **kwargs):
        """
        Create and save invoice document (as *.html file).
        """
        return ContentFile(self.render_document(invoice, **kwargs))

    def create_invoice_model(self, **kwargs):
        Invoice = self.get_invoice_model()
        invoice = Invoice.objects.create(**kwargs)
        document_file = self.generate_document(invoice, **kwargs)
        invoice.document.save(self.get_invoice_filename(invoice), document_file)
        return invoice

    def create_invoice(self, order, **extra_kwargs):
        """
        To create `Invoice` instance, we should have at least one
        instance of `LegalEntity` with `LegalEntityAddress`.
        Some platforms may have couple `LegalEntity`s (with couple
        `LegalEntityAddress`s). In this case needed instances should be
        selected based on order (ordered products).
        """

        legal_entity = self.get_legal_entity()
        if legal_entity and legal_entity.has_addresses:
            number = extra_kwargs.pop('number', None)
            if not number:
                number = self.generate_invoice_number(**extra_kwargs)
            return self.create_invoice_model(
                legal_entity=legal_entity, number=number, order=order, **extra_kwargs
            )
