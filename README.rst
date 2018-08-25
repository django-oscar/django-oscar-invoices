=====================
django-oscar-invoices
=====================

How invoices are generated?
---------------------------

In order to generate invoice it's required to create two model records:

* Merchant account, ``oscar_invoices.abstract_models.AbstractLegalEntity``.
  In contains shop name, seller's business name, website, email, VAT number etc.

* Merchant address, ``oscar_invoices.abstract_models.AbstractLegalEntityAddress``. It's
  quite similar to the order shipping or billing address.

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
