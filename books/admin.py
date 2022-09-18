from django.contrib import admin

# Register your models here.
from .models import Book
from import_export.admin import ImportExportModelAdmin

@admin.register(Book)
class PostImportExport(ImportExportModelAdmin):
    pass