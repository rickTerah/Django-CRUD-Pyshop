from django.contrib import admin
from .models import Product

# Admin Interface
class ProductAdmin(admin.ModelAdmin):
    list_display = (
        'title',
        'price',
        'stock'
    )

# Register your models here.
admin.site.register(Product, ProductAdmin)
