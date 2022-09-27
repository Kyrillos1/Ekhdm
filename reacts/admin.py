from django.contrib import admin

# Register your models here.
from .models import *
from import_export.admin import ImportExportModelAdmin

@admin.register(Comment)
class PostImportExport(ImportExportModelAdmin):
    pass
@admin.register(Save)
class PostImportExport(ImportExportModelAdmin):
    pass
@admin.register(Like)
class PostImportExport(ImportExportModelAdmin):
    pass