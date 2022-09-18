from django.contrib import admin
from .models import Week
from import_export.admin import ImportExportModelAdmin

# admin.site.register(Week)

@admin.register(Week)
class PostImportExport(ImportExportModelAdmin):
    pass