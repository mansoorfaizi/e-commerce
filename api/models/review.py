from django.db import models
from django.contrib.auth import get_user_model
from django.core.validators import MinValueValidator, MaxValueValidator
User = get_user_model()

from .product import Product as Product


class Review (models.Model):
    
    rating = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(5)] , blank=True, null=True )
    comment = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    
    
    
    def __str__(self):
        return f'Review by  {self.user.username} on {self.product.name} - Rating: {self.rating} Stars'
    
    class Meta:
        ordering = ['-created_at']
        
        
        