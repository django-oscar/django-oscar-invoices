Settings
========


``OSCAR_INVOICES_DOCUMENT_ROOT``
--------------------------------

Default: ``documents/``

Location of the document directory, which contains sensitive data and hence
should not be publicly available (as media files).

``OSCAR_INVOICES_FOLDER``
------------------------

Default: ``invoices/%Y/%m/``

The location within the ``MEDIA_ROOT`` folder that is used to store generated invoices.
The folder name can contain date format strings as described in the `Django Docs`_.

.. _`Django Docs`: https://docs.djangoproject.com/en/stable/ref/models/fields/#filefield


``OSCAR_INVOICES_INVOICE_MODEL``
--------------------------------

Default: ``oscar_invoices.Invoice``

Path to the invoice model. Since Oscar does not allow to fork
external applications, in order to customize invoice model you
will need to create it in your project and specify path to it
in the setting.
