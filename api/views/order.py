from rest_framework import viewsets
from api.models.order import Order, OrderItem
from api.serializers.order import OrderSerializer, OrderItemSerializer

class OrderViewset(viewsets.ModelViewSet):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer


class OrderItemViewset(viewsets.ModelViewSet):
    queryset = OrderItem.objects.all()
    serializer_class = OrderItemSerializer
    