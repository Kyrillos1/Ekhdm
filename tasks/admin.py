from django.contrib import admin

# Register your models here.
from .models import *
from import_export.admin import ImportExportModelAdmin

@admin.register(Task)
class PostImportExport(ImportExportModelAdmin):
    pass
@admin.register(Submit)
class PostImportExport(ImportExportModelAdmin):
    pass