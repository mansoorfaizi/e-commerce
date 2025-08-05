from django.db import models
from .product import Product
class ProductImage(models.Model):
    image = models.ImageField(upload_to='product_images/')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    product = models.ForeignKey(
        Product,
        on_delete=models.CASCADE,
        related_name='images'
    )

    def __str__(self):
        return f"Image for {self.product.name} (ID: {self.id})"
    class Meta:
        ordering = ['-created_at']