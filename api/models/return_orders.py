from django.db import models
from .timestamp import TimeStampedModel
from .order import Order

class ReturnOrder(TimeStampedModel):
    STATUS_CHOICES = [
        ('requested', 'Requested'),
        ('approved', 'Approved'),
        ('rejected', 'Rejected'),
    ]    
    order = models.ForeignKey(Order, on_delete=models.CASCADE, related_name='returns')
    reason = models.TextField()
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='requested')

    def __str__(self):
        return f"Return #{self.id} for {self.order}"