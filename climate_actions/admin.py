# Register your models here.
from django.contrib import admin
from import_export import resources
from import_export.admin import ImportExportModelAdmin

from .models import AdaptationAction


class AdaptationActionResource(resources.ModelResource):
    class Meta:
        model = AdaptationAction


class AdaptationActionAdmin(ImportExportModelAdmin):
    resource_class = AdaptationActionResource


admin.site.register(AdaptationAction, AdaptationActionAdmin)
