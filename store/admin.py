from django.contrib import admin
from .models import Product

# Register your models here.
class ProductAdmin(admin.ModelAdmin):
    list_display = ['category', 'product_name', 'price', 'stock', 'modified_date', 'is_available' ]
    prepopulated_fields = {'slug' : ('product_name',)}
    list_editable = ('price', 'stock')
    list_filter = ['category', 'stock']

admin.site.register(Product, ProductAdmin)
