from django.contrib import admin
from import_export.admin import ImportExportModelAdmin
from .models import *

# admin.site.register(Profile)
admin.site.register([ Message])
# admin.site.register()



@admin.register(Profile)
class PostImportExport(ImportExportModelAdmin):
    pass
@admin.register(Church)
class PostImportExport(ImportExportModelAdmin):
    pass
@admin.register(Family)
class PostImportExport(ImportExportModelAdmin):
    pass
