from rest_framework import viewsets
from api.models.shipping_address import ShippingAddress
from api.serializers.shipping_address import ShippingAddress

class ShippingAdressViewset(viewsets.ModelViewSet):
    queryset = ShippingAddress.objects.all()
    serializer_class=ShippingAddress
