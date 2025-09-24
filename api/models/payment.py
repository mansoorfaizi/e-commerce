from django.db import models
from .timestamp import TimeStampedModel
from .order import Order

class Payment(TimeStampedModel):
    method = models.CharField(max_length=255)
    status = models.BooleanField()
    transaction_id = models.CharField(max_length=255)
    date = models.DateField()
    total_price = models.DecimalField(max_digits=10, decimal_places=2)
    order = models.ForeignKey(Order, on_delete=models.CASCADE, related_name='payments')

    def __str__(self):
        return f"Payment {self.transaction_id} for Order {self.order.id}"