from django.dispatch import receiver
from oscar.apps.order.signals import order_placed
from oscar.core.loading import get_class

InvoiceCreator = get_class('oscar_invoices.utils', 'InvoiceCreator')


@receiver(order_placed)
def receive_order_placed(sender, order, **kwargs):
    InvoiceCreator().create_invoice(order)
