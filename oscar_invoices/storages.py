from django.core.files.storage import FileSystemStorage
from django.utils.deconstruct import deconstructible
from django.utils.functional import cached_property

from . import app_settings


@deconstructible
class DocumentsStorage(FileSystemStorage):
    """
    Custom filesystem storage for storing documents outside of media directory
    (destination folder - `settings.OSCAR_INVOICES_DOCUMENT_ROOT`) and
    restricting their public access via URL.
    """

    def __init__(self, *args, **kwargs):
        super(DocumentsStorage, self).__init__(*args, **kwargs)
        self._location = app_settings.OSCAR_INVOICES_DOCUMENTS_ROOT

    def _clear_cached_properties(self, setting, **kwargs):
        if setting == 'OSCAR_INVOICES_DOCUMENTS_ROOT':
            self.__dict__.pop('base_location', None)
            self.__dict__.pop('location', None)

        elif setting == 'FILE_UPLOAD_PERMISSIONS':
            self.__dict__.pop('file_permissions_mode', None)

        elif setting == 'FILE_UPLOAD_DIRECTORY_PERMISSIONS':
            self.__dict__.pop('directory_permissions_mode', None)

    @cached_property
    def base_location(self):
        return self._value_or_setting(self._location, app_settings.OSCAR_INVOICES_DOCUMENTS_ROOT)

    def url(self, name):
        raise ValueError("This file is not accessible via a URL.")
