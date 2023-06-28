from django.contrib import admin
from django.utils.html import format_html
from products.models import Category, Product


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    pass


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    @admin.display(description="category", ordering="category__name")
    def category_name(self, obj):
        return obj.category.name

    @admin.display(description="image", ordering="image")
    def image_html(self, obj):
        return format_html(f"<img src='{obj.image_src}' width='100' />")

    list_display = ("name", "category_name", "price", "image_html")
    ordering = ("name", "category__name")
    search_fields = ("name", "category__name")
    list_per_page = 10
