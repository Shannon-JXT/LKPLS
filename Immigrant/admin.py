from import_export.admin import ImportExportModelAdmin
from import_export import resources
from django.contrib import admin
from .models import Culture, Region, Event

class RegionResource(resources.ModelResource):
    class Meta:
        model = Region
        export_order = ('id', 'year', 'region_name', 'country_name', 'migrant_num')

class EventResource(resources.ModelResource):
    class Meta:
        model = Event
        export_order = ('id', 'title', 'description', 'link', 'start_date', 'end_date')

# Register your models here.
@admin.register(Culture)
class CountryAdmin(admin.ModelAdmin):
    list_display = ('id', 'country_name', 'create_time', 'last_updated_time')
    ordering = ("id",)

@admin.register(Region)
class RegionAdmin(ImportExportModelAdmin):
    list_display = ('id', 'year', 'region_name', 'country_name', 'migrant_num')
    ordering = ('id',)

@admin.register(Event)
class EventAdmin(ImportExportModelAdmin):
    list_display = ('id', 'title', 'start_date', 'end_date',)
    ordering = ('id',)
