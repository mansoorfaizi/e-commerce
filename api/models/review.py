from django.db import models
from django.contrib.auth import get_user_model
User = get_user_model()

from .product import Product as Product


class Review (models.Model):
    id = models.AutoField(primary_key=True)
    rating = models.IntegerField()
    comment = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    
    
    
    def __str__(self):
        return f'Review by  {self.user.username} on {self.product.name} - Rating: {self.rating} Stars'
    
    class Meta:
        ordering = ['-created_at']
        
        
        