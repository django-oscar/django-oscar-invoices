from django.conf import settings

OSCAR_INVOICES_DOCUMENTS_ROOT = getattr(settings, 'OSCAR_INVOICES_DOCUMENTS_ROOT', 'documents/')
