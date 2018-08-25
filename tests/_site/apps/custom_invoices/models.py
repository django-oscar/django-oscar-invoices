from django.db import models
from django.utils.translation import ugettext_lazy as _

from oscar_invoices.abstract_models import AbstractInvoice


class CustomInvoice(AbstractInvoice):
    """
    An Custom invoice for tests.
    """

    legal_entity = models.ForeignKey(
        'oscar_invoices.LegalEntity',
        on_delete=models.CASCADE,
        related_name='custom_invoices',
        verbose_name=_('Legal Entity'))

    order = models.OneToOneField(
        'order.Order', verbose_name=_('Order'), related_name='custom_invoice',
        null=True, blank=True, on_delete=models.SET_NULL)

    additional_test_field = models.CharField(
        help_text='This field added just for test purposes',
        max_length=120)

    class Meta:
        app_label = 'custom_invoices'
        verbose_name = _('Custom invoice')
        verbose_name_plural = _('Custom invoices')
