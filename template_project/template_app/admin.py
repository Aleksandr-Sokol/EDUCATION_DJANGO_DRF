from django.contrib import admin
from .models import Price, Brand, Clothes


@admin.register(Brand)
class BrandAdmin(admin.ModelAdmin):
    list_display = ('title', 'country')


@admin.register(Clothes)
class ClothesAdmin(admin.ModelAdmin):
    list_display = ('title', 'size', 'brand')


@admin.register(Price)
class PriceAdmin(admin.ModelAdmin):
    list_display = ('value', 'date', 'clothes')
