from django.db import models
from .Order import Order
from .timestamp import TimeStampedModel
from .product import Product

class OrderItem(TimeStampedModel):
    quantity = models.IntegerField()
    price_at_purchase = models.DecimalField(max_digits=10, decimal_places=2)
    order = models.ForeignKey(Order, on_delete=models.CASCADE, related_name='order_items')
    product = models.ForeignKey(Product, on_delete=models.SET_NULL, null=True, related_name='order_items')

    def __str__(self):
        return f"{self.quantity} x {self.product.name} for Order #{self.order.id}"