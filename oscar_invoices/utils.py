from oscar.core.loading import get_model

Invoice = get_model('oscar_invoices', 'Invoice')
LegalEntity = get_model('oscar_invoices', 'LegalEntity')


class InvoiceNumberGenerator(object):
    """
    Simple object for generating invoice numbers.
    """

    def invoice_number(self):
        return Invoice.get_last_invoice_number() + 1


def create_invoice(order, invoice_number_generator=None):
    """
    To create `Invoice` instance, we should have at least one
    instance of `LegalEntity` with `LegalEntityAddress`.
    Some platforms may have couple `LegalEntity`s (with couple
    `LegalEntityAddress`s). In this case needed instances should be
    selected based on order (ordered products).
    """
    legal_entity = LegalEntity.objects.first()
    if legal_entity and legal_entity.has_addresses:
        invoice_number_generator = invoice_number_generator or InvoiceNumberGenerator
        invoice_number = invoice_number_generator().invoice_number()

        invoice = Invoice.objects.create(
            legal_entity=legal_entity, number=invoice_number, order=order)
        invoice.generate_and_save_document()
