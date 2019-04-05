=====================
django-oscar-invoices
=====================

Quickstart
==========

Installation
------------

.. code-block:: console

    $ pip install django-oscar-invoices


Setup
-----

1. Add ``oscar_invoices`` to the ``INSTALLED_APPS`` variable of your
   project's ``settings.py``.

2. Sync the database using ``python manage.py migrate``.

3. Create instances of ``LegalEntity`` and ``LegalEntityAddress``.

4. Integrate ``InvoiceCreator`` in your checkout process.


By default, we generate only HTML invoice document and allow user to decide how to
generate PDF documents. You can integrate `python-pdfkit`_, `WeasyPrint`_, `xhtml2pdf`_,
`reportlab`_ or another library of your choice.

.. _`python-pdfkit`: https://github.com/JazzCore/python-pdfkit
.. _`WeasyPrint`: https://github.com/Kozea/WeasyPrint
.. _`xhtml2pdf`: https://github.com/xhtml2pdf/xhtml2pdf
.. _`reportlab`: https://www.reportlab.com/

Since documents contains sensitive data, we store them out of the media folder and
do not provide public access via URL. For this purpose, we use custom storage class
``oscar_invoices.storages.DocumentsStorage``, invoice documents placed into the
nested folder ``settings.OSCAR_INVOICES_UPLOAD_FOLDER`` and available for the admin users via
dashboard order list.


You can find more information in documentation_.

.. _documentation: https://django-oscar-invoices.readthedocs.io


Sandbox
-------

Sandbox environment set up to automatically create invoices on checkout.
But for this, instances of ``LegalEntity`` and ``LegalEntityAddress`` must be created
(from ``admin`` site) before order placement.