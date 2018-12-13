from django.contrib import admin

from oscar.core.loading import get_model

from .models import is_custom_invoice_model

LegalEntity = get_model('oscar_invoices', 'LegalEntity')
LegalEntityAddress = get_model('oscar_invoices', 'LegalEntityAddress')

admin.site.register(LegalEntity)
admin.site.register(LegalEntityAddress)


class InvoiceAdmin(admin.ModelAdmin):
    exclude = ("document",)

if not is_custom_invoice_model:
    Invoice = get_model('oscar_invoices', 'Invoice')
    admin.site.register(Invoice, InvoiceAdmin)
