from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from django.conf import settings

from .product import Product as Product
from .timestamp import TimeStampedModel


class Review(TimeStampedModel):
    rating = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(5)], blank=True, null=True)
    comment = models.TextField()
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    
    def __str__(self):
        return f'Review by  {self.user.username} on {self.product.name} - Rating: {self.rating} Stars'
    
    class Meta:
        ordering = ['-created_at']
        
        
        