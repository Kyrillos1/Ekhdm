from django.contrib import admin

# Register your models here.
from .models import *
from comments.models import Comment
from import_export.admin import ImportExportModelAdmin


# admin.site.register(Tag)

@admin.register(Quiz)
class PostImportExport(ImportExportModelAdmin):
    pass
@admin.register(Question)
class PostImportExport(ImportExportModelAdmin):
    pass
@admin.register(Result)
class PostImportExport(ImportExportModelAdmin):
    pass
@admin.register(UserAns)
class PostImportExport(ImportExportModelAdmin):
    pass
