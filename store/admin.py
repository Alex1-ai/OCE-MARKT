from django.contrib import admin

from .models import Product
# Register your models here.


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ["product_name"]}
    list_display = ['product_name', 'slug',
                    'price', 'image', 'stock', 'category', 'is_available', 'created_date', 'modified_date']