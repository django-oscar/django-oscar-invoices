``OSCAR_INVOICES_DOCUMENT_ROOT``
--------------------------------

Default: ``documents/``

Location of the document directory, which contains sensitive data and hence
should not be publicly available (as media files).

``OSCAR_INVOICES_FOLDER``
------------------------

Default: ``invoices/%Y/%m/``

The location within the ``MEDIA_ROOT`` folder that is used to store product images.
The folder name can contain date format strings as described in the `Django Docs`_.

.. _`Django Docs`: https://docs.djangoproject.com/en/stable/ref/models/fields/#filefield

``OSCAR_INVOICE_GENERATE_AFTER_ORDER_PLACED``
---------------------------------------------

Default: ``False``

Specifies if an invoice (instance of ``Invoice`` model) will be created automatically
after order placement. If set to ``True``, invoice will be created in case when
at least one instance of each ``LegalEntity`` and ``LegalEntityAddress`` models was created.