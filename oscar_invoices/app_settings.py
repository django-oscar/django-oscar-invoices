from django.conf import settings

OSCAR_INVOICES_DOCUMENTS_ROOT = getattr(settings, 'OSCAR_INVOICES_DOCUMENTS_ROOT', 'documents/')

OSCAR_INVOICES_UPLOAD_FOLDER = getattr(settings, 'OSCAR_INVOICES_UPLOAD_FOLDER', 'invoices/%Y/%m/')

OSCAR_INVOICES_GENERATE_AFTER_ORDER_PLACED = getattr(settings, 'OSCAR_INVOICES_GENERATE_AFTER_ORDER_PLACED', False)

OSCAR_INVOICE_INVOICE_MODEL = getattr(settings, 'OSCAR_INVOICE_INVOICE_MODEL', 'oscar_invoices.Invoice')
