from django.dispatch import receiver

from oscar.apps.order.signals import order_placed

from . import app_settings
from .utils import InvoiceCreator


if app_settings.OSCAR_INVOICES_GENERATE_AFTER_ORDER_PLACED:
    @receiver(order_placed)
    def receive_order_placed(sender, order, **kwargs):
        InvoiceCreator().create_invoice(order)
