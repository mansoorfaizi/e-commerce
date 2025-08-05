from django.contrib import admin
from .models.product import Product
from .models.productImage import ProductImage

admin.site.register(Product)
admin.site.register(ProductImage)
