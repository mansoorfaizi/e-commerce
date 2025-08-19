from django.contrib import admin
from .models.product import Product
from .models.productImage import ProductImage
from .models.review import Review  
from .models.shippingAddress import ShippingAddress 



admin.site.register(Product)
admin.site.register(ProductImage)
admin.site.register(Review)
admin.site.register(ShippingAddress)

