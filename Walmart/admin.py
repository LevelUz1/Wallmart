from django.contrib import admin
from .models import Oluvchi, Sotuvchi, Mahsulot

@admin.register(Oluvchi)
class OluvchiAdmin(admin.ModelAdmin):
    list_display = ('ism', 'yosh')

@admin.register(Sotuvchi)
class SotuvchiAdmin(admin.ModelAdmin):
    list_display = ('ism', 'familya', 'email')

@admin.register(Mahsulot)
class MahsulotAdmin(admin.ModelAdmin):
    list_display = ('nom', 'rang', 'narh', 'oluvchi', 'sotuvchi')
