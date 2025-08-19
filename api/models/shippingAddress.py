from django.db import models
from django.contrib.auth import get_user_model
User = get_user_model()


class ShippingAddress(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    full_address = models.TextField()
    city = models.CharField( max_length=100)
    country = models.CharField(max_length=100)
    postel_code = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    
    def __str__(self):
        return f'Shipping Address for {self.user.username} - {self.city}, {self.country}  ({self.postel_code})'
    
