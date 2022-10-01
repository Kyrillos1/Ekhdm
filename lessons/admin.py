from django.contrib import admin

# Register your models here.
from .models import Lesson, LessonType
from import_export.admin import ImportExportModelAdmin


# admin.site.register(Tag)

@admin.register(Lesson)
class PostImportExport(ImportExportModelAdmin):
    pass
@admin.register(LessonType)
class PostImportExport(ImportExportModelAdmin):
    pass