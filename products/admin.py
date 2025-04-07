from django.contrib import admin
from .models import Product, Brand

# Register your models here.

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):

    list_display = (
        'sku',
        'name',
        'brand_category',
        'rating',
        'price',
        'image',
    )
    search_fields =['name']
    list_filter = ('sku',)
    ordering = ('sku',)

class BrandAdmin(admin.ModelAdmin):

    list_display = (
        'name',
        'other_name',
    )
    search_fields =['name']
    list_filter = ('name',)
    ordering = ('name',)

#admin.site.register(Product)
admin.site.register(Brand, BrandAdmin)