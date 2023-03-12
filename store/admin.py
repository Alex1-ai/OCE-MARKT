from django.contrib import admin

from .models import Product, Variation
# Register your models here.


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ["product_name"]}
    list_display = ['product_name', 'slug',
                    'price', 'image', 'stock', 'category', 'is_available', 'created_date', 'modified_date']


@admin.register(Variation)
class VariationAdmin(admin.ModelAdmin):
    list_display = ['product', 'variation_category',
                    'variation_value', 'is_active', 'created_date', 'updated_date']
    list_filter = ['product', 'variation_category',
                   'variation_value']
    list_editable = ['is_active']
