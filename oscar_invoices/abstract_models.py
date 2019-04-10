from django.conf import settings
from django.db import models
from django.utils.translation import ugettext_lazy as _
from django.urls import reverse

from phonenumber_field.modelfields import PhoneNumberField

from oscar.apps.address.abstract_models import AbstractAddress

from . import app_settings
from .storages import DocumentsStorage


class AbstractLegalEntity(models.Model):
    """
    Represents LegalEntity - merchant (company or individual) which we issue
    invoice on behalf of.
    """
    shop_name = models.CharField(_('Shop name'), max_length=255, null=True, blank=True)
    business_name = models.CharField(_('Business name'), max_length=255, db_index=True)
    vat_number = models.CharField(_('VAT identification number'), max_length=20)
    logo = models.ImageField(
        _('Logo'), upload_to=settings.OSCAR_IMAGE_FOLDER, max_length=255, null=True, blank=True)
    email = models.EmailField(_('Email'), null=True, blank=True)
    web_site = models.URLField(_('Website'), null=True, blank=True)

    class Meta:
        abstract = True
        app_label = 'oscar_invoices'
        verbose_name = _('Legal Entity')
        verbose_name_plural = _('Legal Entities')

    def __str__(self):
        return self.business_name

    @property
    def has_addresses(self):
        return self.addresses.exists()


class AbstractLegalEntityAddress(AbstractAddress):
    """
    Represents Address of LegalEntity.

    Used in Invoices.
    """
    legal_entity = models.ForeignKey(
        'oscar_invoices.LegalEntity',
        on_delete=models.CASCADE,
        related_name='addresses',
        verbose_name=_('Legal Entity'))

    phone_number = PhoneNumberField(_('Phone number'), blank=True)
    fax_number = PhoneNumberField(_('Fax number'), blank=True)

    class Meta:
        abstract = True
        app_label = 'oscar_invoices'
        verbose_name = _('Legal Entity Address')
        verbose_name_plural = _('Legal Entity Addresses')


class AbstractInvoice(models.Model):
    """
    An Invoice.
    """

    legal_entity = models.ForeignKey(
        'oscar_invoices.LegalEntity',
        on_delete=models.CASCADE,
        related_name='invoices',
        verbose_name=_('Legal Entity'))

    number = models.CharField(
        _('Invoice number'), max_length=128, unique=True)

    order = models.OneToOneField(
        'order.Order', verbose_name=_('Order'), related_name='invoice',
        null=True, blank=True, on_delete=models.SET_NULL)

    notes = models.TextField(_('Notes for invoice'), null=True, blank=False)

    document = models.FileField(
        _('Document'), upload_to=app_settings.OSCAR_INVOICES_UPLOAD_FOLDER,
        blank=True, null=True, max_length=255, storage=DocumentsStorage())

    class Meta:
        abstract = True
        app_label = 'oscar_invoices'
        verbose_name = _('Invoice')
        verbose_name_plural = _('Invoices')

    def get_absolute_url(self):
        return reverse('oscar_invoices:invoice', args=(self.pk,))

    def __str__(self):
        if self.order:
            order_number = self.order.number
            return _(
                'Invoice #%(invoice_number)s for order #%(order_number)s'
            ) % {'invoice_number': self.number, 'order_number': order_number}

        return _(
            'Invoice #%(invoice_number)s') % {'invoice_number': self.number}
