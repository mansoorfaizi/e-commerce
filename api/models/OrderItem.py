from django.db import models

# Assuming Product and Order are already defined like this:
# from .models import Product, Order

class OrderItem(models.Model):
    id = models.AutoField(primary_key=True)
    quantity = models.IntegerField()
    price_at_purchase = models.DecimalField(max_digits=10, decimal_places=2)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    order = models.ForeignKey('Order', on_delete=models.CASCADE, related_name='order_items')
    product = models.ForeignKey('Product', on_delete=models.SET_NULL, null=True, related_name='order_items')

    def __str__(self):
        return f"{self.quantity} x {self.product.name} for Order #{self.order.id}"