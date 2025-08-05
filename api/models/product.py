from django.db import models

class Product(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    price = models.DecimalField(
        max_digits=10, 
        decimal_places=3
    )
    stock_quantity = models.PositiveIntegerField()
    warranty_period = models.CharField(max_length=100)
    discount = models.DecimalField(
        max_digits=5,
        decimal_places=2,
        default=0
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.name
    class Meta:
        ordering = ['-created_at'] 