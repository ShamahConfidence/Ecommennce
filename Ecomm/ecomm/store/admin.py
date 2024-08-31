from django.contrib import admin
from .models import Product, CartItem


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ["name","price", "stock", "img_url"]


@admin.register(CartItem)
class CartAdmin(admin.ModelAdmin):
    list_display = ["product", "quantity", "added_at"]