from django.contrib import admin

# Register your models here.
from .models import Post
from comments.models import Comment
from import_export.admin import ImportExportModelAdmin


# admin.site.register(Tag)

@admin.register(Post)
class PostImportExport(ImportExportModelAdmin):
    pass