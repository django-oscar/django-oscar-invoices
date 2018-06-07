from oscar.core.loading import is_model_registered

from oscar_invoices.abstract_models import AbstractInvoice, AbstractLegalEntity, AbstractLegalEntityAddress

__all__ = []

if not is_model_registered('oscar_invoices', 'Invoices'):
    class Invoice(AbstractInvoice):
        pass

    __all__.append('Invoice')


if not is_model_registered('oscar_invoices', 'LegalEntity'):
    class LegalEntity(AbstractLegalEntity):
        pass

    __all__.append('LegalEntity')


if not is_model_registered('oscar_invoices', 'LegalEntityAddress'):
    class LegalEntityAddress(AbstractLegalEntityAddress):
        pass

    __all__.append('LegalEntityAddress')
