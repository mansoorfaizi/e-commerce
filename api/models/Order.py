from django.db import models
from .timestamp import TimeStampedModel
from django.contrib.auth.models import User
from api.models.product import Product


class Order(TimeStampedModel):
    date = models.DateField()
    status = models.CharField(max_length=100)
    total_price = models.DecimalField(max_digits=10, decimal_places=2)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='orders')

    def __str__(self):
        return f"Order #{self.id} - {self.user.username} - {self.status}"


class OrderItem(TimeStampedModel):
    quantity = models.IntegerField()
    price_at_purchase = models.DecimalField(max_digits=10, decimal_places=2)
    order = models.ForeignKey(Order, on_delete=models.CASCADE, related_name='order_items')
    product = models.ForeignKey(Product, on_delete=models.SET_NULL, null=True, related_name='order_items')

    def __str__(self):
        return f"{self.quantity} x {self.product.name} for Order #{self.order.id}"