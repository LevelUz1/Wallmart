from django.contrib import admin
from import_export.admin import ImportExportModelAdmin
from .models import Oluvchi, Sotuvchi, Mahsulot


def levelbe(modeladmin, request, queryset):
    queryset.update(age=50)


@admin.register(Oluvchi)
class OluvchiAdmin(ImportExportModelAdmin):
    list_display = ('ism', 'yosh')
    list_filter = ('ism', 'yosh')
    search_fields = ('ism', 'yosh')


@admin.register(Sotuvchi)
class SotuvchiAdmin(ImportExportModelAdmin):
    list_display = ('ism', 'familya', 'email', 'yosh')

@admin.register(Mahsulot)
class MahsulotAdmin(ImportExportModelAdmin):
    list_display = ('nom', 'rang', 'narh', 'oluvchi', 'sotuvchi')
    autocomplete_fields = ('oluvchi',)
