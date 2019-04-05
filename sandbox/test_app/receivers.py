from django.dispatch import receiver

from oscar.apps.order.signals import order_placed

from oscar_invoices.utils import InvoiceCreator


@receiver(order_placed)
def receive_order_placed(sender, order, **kwargs):
    InvoiceCreator().create_invoice(order)
