from django.contrib import admin

from oscar.core.loading import get_model

Invoice = get_model('oscar_invoices', 'Invoice')
LegalEntity = get_model('oscar_invoices', 'LegalEntity')
LegalEntityAddress = get_model('oscar_invoices', 'LegalEntityAddress')

admin.site.register(Invoice)
admin.site.register(LegalEntity)
admin.site.register(LegalEntityAddress)
