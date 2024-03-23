import factory
from oscar.core.loading import get_model

__all__ = ['LegalEntityAddressFactory', 'LegalEntityFactory']


class LegalEntityFactory(factory.django.DjangoModelFactory):
    business_name = 'Test Company'
    company_number = 'test-company-number'

    class Meta:
        model = get_model('oscar_invoices', 'LegalEntity')


class LegalEntityAddressFactory(factory.django.DjangoModelFactory):
    legal_entity = factory.SubFactory(LegalEntityFactory)
    line1 = '1 Egg Street'
    line2 = 'London'
    postcode = 'N12 9RE'
    country = factory.SubFactory('oscar.test.factories.CountryFactory')

    class Meta:
        model = get_model('oscar_invoices', 'LegalEntityAddress')
