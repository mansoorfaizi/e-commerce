from django.contrib import admin
from api.models.category import Category
from api.models.Order  import Order, OrderItem
from api.models.Payment import Payment
from .models.product import Product, ProductImage
from api.models.ReturnOrders import ReturnOrder
from .models.review import Review
from api.models.shipping_address import ShippingAddress
from .models.support_chat import SupportChat, Conversation


admin.site.register(Product)
admin.site.register(ProductImage)
admin.site.register(Review)
admin.site.register(Conversation)
admin.site.register(SupportChat)
admin.site.register(Order)
admin.site.register(OrderItem)
