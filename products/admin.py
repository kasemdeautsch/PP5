from django.contrib import admin
from .models import Product, Brand


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = (
        'sku',
        'name',
        'brand',
        'rating',
        'price',
        'image',
    )
    search_fields = ['name', 'sku']
    list_filter = ('sku',)
    ordering = ('sku',)


class BrandAdmin(admin.ModelAdmin):

    list_display = (
        'name',
        'other_name',
    )
    search_fields = ['name']
    list_filter = ('name',)
    ordering = ('name',)


admin.site.register(Brand, BrandAdmin)
