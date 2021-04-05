from django.contrib import admin
from webapp.models import Product
# Register your models here.


class ProductAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'category', 'description', 'remainder', 'price']
    list_filter = ['name']
    search_fields = ['name', 'price']
    fields = ['id', 'name', 'category', 'description', 'remainder', 'price']
    readonly_fields = ['id']


admin.site.register(Product, ProductAdmin)