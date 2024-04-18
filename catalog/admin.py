from django.contrib import admin

from catalog.models import Category, Product, Version


# Register your models here.

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ("id", "name",)


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ("id", "name", "purchase_price", "category", "created_at", "updated_at")
    list_filter = ("category",)
    search_fields = ("name", "description",)


@admin.register(Version)
class VerionAdmin(admin.ModelAdmin):
    list_display = ("product", "version_number", "version_name", "is_actual",)
