from django.db import models
from .timestamp import TimeStampedModel
from .category import Category

class Product(TimeStampedModel):
    category = models.ForeignKey(
        Category,
        null=True,
        blank=True,
        on_delete=models.CASCADE,
        related_name='products'
    )
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
    
    def __str__(self):
        return self.name
    class Meta:
        ordering = ['-created_at'] 




class ProductImage(TimeStampedModel):
    image = models.ImageField(upload_to='product_images/')
    product = models.ForeignKey(
        Product,
        on_delete=models.CASCADE,
        related_name='images'
    )

    def __str__(self):
        return f"Image for {self.product.name} (ID: {self.id})"
    
    class Meta:
        ordering = ['-created_at']