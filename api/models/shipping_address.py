from .timestamp import TimeStampedModel
from django.db import models
from django.conf import settings


class ShippingAddress(TimeStampedModel):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    full_address = models.TextField()
    city = models.CharField( max_length=100)
    country = models.CharField(max_length=100)
    postel_code = models.CharField(max_length=100)
    latitude = models.FloatField(null=True, blank=True)
    longitude = models.FloatField(null=True, blank=True)

    def __str__(self):
        return f'Shipping Address for {self.user.username} - {self.city}, {self.country}  ({self.postel_code})'