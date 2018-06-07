from django.dispatch import receiver

from oscar.apps.order.signals import order_placed
from .utils import create_invoice


@receiver(order_placed)
def receive_order_placed(sender, order, **kwargs):
    create_invoice(order)
