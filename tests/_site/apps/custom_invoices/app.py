from oscar.core.application import Application


class CustomInvoicesApplication(Application):
    name = 'custom_invoices'


application = CustomInvoicesApplication()
