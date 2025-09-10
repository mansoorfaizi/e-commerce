from rest_framework import serializers
from api.models.shipping_address import ShippingAddress



class ShippingAddressSerializer(serializers.ModelSerializer):
    class Meta:
        model = ShippingAddress
        fields = "__all__" 