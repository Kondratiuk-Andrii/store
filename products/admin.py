from django.contrib import admin

from products.models import Basket, Product, ProductCategory


@admin.register(ProductCategory)
class ProductCategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'description', 'slug')
    prepopulated_fields = {'slug': ('name',)}


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'quantity', 'category')
    fields = ('name', 'description', ('price', 'quantity'), 'stripe_product_price_id', 'image', 'category')
    search_fields = ('name', 'category__name')
    ordering = ('name',)


class BasketAdmin(admin.TabularInline):
    model = Basket
    fields = ('product', 'quantity', 'created_timestamp')
    readonly_fields = ('created_timestamp',)
    extra = 0
