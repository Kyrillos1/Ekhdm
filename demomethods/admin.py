from django.contrib import admin

# Register your models here.
from .models import Demomethod, Review, Tag
from import_export.admin import ImportExportModelAdmin

@admin.register(Demomethod)
class PostImportExport(ImportExportModelAdmin):
    pass
# admin.site.register(Demomethod)
# admin.site.register(Review)
@admin.register(Review)
class PostImportExport(ImportExportModelAdmin):
    pass
# admin.site.register(Tag)
@admin.register(Tag)
class PostImportExport(ImportExportModelAdmin):
    pass