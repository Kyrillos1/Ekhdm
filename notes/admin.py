from django.contrib import admin

# Register your models here.
from import_export.admin import ImportExportModelAdmin
from .models import *
@admin.register(Note)
class PostImportExport(ImportExportModelAdmin):
    pass