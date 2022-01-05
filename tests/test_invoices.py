import os
import shutil
import threading
import time
from datetime import date

import pytest
from django.conf import settings
from django.test import TransactionTestCase
from mock import patch
from oscar.core.loading import get_class, get_model
from oscar.test.factories import CountryFactory, UserFactory, create_order
from oscar.test.testcases import WebTestCase
from oscar.test.utils import run_concurrently

from oscar_invoices import app_settings
from oscar_invoices.utils import InvoiceCreator

from ._site.apps.custom_invoices.models import CustomInvoice
from .factories import LegalEntityAddressFactory, LegalEntityFactory

Invoice = get_model('oscar_invoices', 'Invoice')
LegalEntity = get_model('oscar_invoices', 'LegalEntity')
LegalEntityAddress = get_model('oscar_invoices', 'LegalEntityAddress')
Partner = get_model('partner', 'Partner')
ProductClass = get_model('catalogue', 'ProductClass')


OSCAR_INVOICES_FOLDER_FORMATTED = 'invoices/{0}/{1:02d}/'.format(date.today().year, date.today().month)
FULL_PATH_TO_INVOICES = os.path.join(app_settings.OSCAR_INVOICES_DOCUMENTS_ROOT, OSCAR_INVOICES_FOLDER_FORMATTED)


class TestInvoiceMixin:

    def setUp(self):
        super().setUp()
        self.user = UserFactory()

        LegalEntityAddressFactory(
            legal_entity=LegalEntityFactory(),
            country=CountryFactory(),
        )

    def tearDown(self):
        super().tearDown()
        # Remove `OSCAR_INVOICE_FOLDER` after each test
        if os.path.exists(FULL_PATH_TO_INVOICES):
            shutil.rmtree(FULL_PATH_TO_INVOICES)


class TestInvoice(TestInvoiceMixin, WebTestCase):

    def setUp(self):
        super().setUp()
        self.order = create_order(number='000042', user=self.user)

    def _test_invoice_is_created(self, order_number='000043'):
        order = create_order(number=order_number, user=self.user)
        InvoiceCreator().create_invoice(order)
        assert Invoice.objects.exists()
        invoice = Invoice.objects.first()
        return invoice

    def test_invoice_cannot_be_created_without_legal_entity(self):
        LegalEntity.objects.all().delete()

        assert not Invoice.objects.exists()
        InvoiceCreator().create_invoice(self.order)
        assert not Invoice.objects.exists()

    def test_invoice_cannot_be_created_without_legal_entity_address(self):
        LegalEntityAddress.objects.all().delete()

        assert not Invoice.objects.exists()
        InvoiceCreator().create_invoice(self.order)
        self.assertFalse(Invoice.objects.exists())

    def test_invoice_can_be_created_with_legal_entity_and_its_address(self):
        assert not Invoice.objects.exists()
        InvoiceCreator().create_invoice(self.order)
        assert Invoice.objects.exists()
        invoice = Invoice.objects.first()
        # Document created and saved
        assert invoice.document is not None

    def test_invoice_creation_based_on_settings(self):
        invoice = self._test_invoice_is_created()
        # Document created and saved
        assert invoice.document is not None

    def test_invoice_document_is_not_accessible_via_url(self):
        invoice = self._test_invoice_is_created()

        another_user = UserFactory(username='another_user')
        staff_user = UserFactory(is_staff=True)
        superuser = UserFactory(is_superuser=True)

        # Invoice document is not accessible via url for any user
        for user in [self.user, another_user, staff_user, superuser]:
            with pytest.raises(ValueError, match='This file is not accessible via a URL.'):
                self.app.get(invoice.document.url, user=user)

    def test_invoice_was_saved_to_correct_folder(self):
        order_number = 'TEST_number_000d5'
        invoice = self._test_invoice_is_created(order_number=order_number)

        file_names = os.listdir(FULL_PATH_TO_INVOICES)
        assert len(file_names) == 1  # Only one file here
        invoice_file_name = 'invoice_{}.html'.format(invoice.number)
        assert invoice_file_name in file_names

        if os.path.exists(settings.MEDIA_ROOT):
            media_file_names = os.listdir(settings.MEDIA_ROOT)
            assert invoice_file_name not in media_file_names

    def test_default_invoice_model_used(self):
        order_number = 'TEST_number_000d6'
        invoice = self._test_invoice_is_created(order_number=order_number)
        assert isinstance(invoice, Invoice)

    @patch('oscar_invoices.app_settings.OSCAR_INVOICES_INVOICE_MODEL', 'custom_invoices.CustomInvoice')
    def test_custom_invoice_model_used(self, *args, **kwargs):
        order_number = 'TEST_number_000d6'
        order = create_order(number=order_number, user=self.user)
        InvoiceCreator().create_invoice(order)
        assert CustomInvoice.objects.exists()

    def test_str_method_of_invoice_model_instance(self):
        """
        Checks correct representation of `Invoice` instance
        (e.g. in invoices list in the admin site).
        """
        order_number = '0000042'
        order = create_order(number=order_number, user=self.user)
        invoice = InvoiceCreator().create_invoice(order)
        assert str(invoice) == 'Invoice #{} for order #{}'.format(invoice.number, order_number)

    def test_str_method_of_invoice_model_instance_when_order_is_deleted(self):
        """
        Checks correct representation of `Invoice` instance
        (E.g. in invoices list in the admin site) when related order
        is deleted.
        """
        order_number = '0000043'
        order = create_order(number=order_number, user=self.user)
        invoice = InvoiceCreator().create_invoice(order)
        order.delete()
        invoice.refresh_from_db()
        assert str(invoice) == 'Invoice #{}'.format(invoice.number)

    def test_invoice_creator_loading(self):
        assert get_class('oscar_invoices.utils', 'InvoiceCreator') == InvoiceCreator


class TestConcurrentInvoiceCreation(TestInvoiceMixin, TransactionTestCase):

    def setUp(self):
        super().setUp()
        # Next needed to prevent `MultipleObjectsReturned` error during concurrent invoices creation
        ProductClass.objects.create(name='Dùｍϻϒ item class')
        Partner.objects.create(name='')

    def test_concurrent_invoice_creation(self):
        num_threads = 5
        creator = InvoiceCreator()

        org_create_invoice = InvoiceCreator.create_invoice

        def new_create_invoice(order, **kwargs):
            time.sleep(0.5)
            return org_create_invoice(creator, order, **kwargs)

        def worker():
            order_number = threading.current_thread().name
            order = create_order(number=order_number, user=self.user)
            new_create_invoice(order)

        exceptions = run_concurrently(worker, num_threads=num_threads)

        assert len(exceptions) == 0
        assert Invoice.objects.count() == 5
