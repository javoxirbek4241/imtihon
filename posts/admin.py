

from django.contrib import admin
from .models import Category, Product, Comment


class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name']
    search_fields = ['name']


class ProductAdmin(admin.ModelAdmin):
    list_display = ['title', 'category', 'user', 'price', 'stock', 'is_available', 'created_at']
    list_filter = ['category', 'is_available', 'user']
    search_fields = ['title', 'desc']


admin.site.register(Category, CategoryAdmin)
admin.site.register(Product, ProductAdmin)
admin.site.register(Comment)

