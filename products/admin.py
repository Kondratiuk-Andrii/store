from django.contrib import admin

from products.models import Product, ProductCategory

# Register your models here.

admin.site.register(Product)


class ProductCategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name',)}


admin.site.register(ProductCategory, ProductCategoryAdmin)
