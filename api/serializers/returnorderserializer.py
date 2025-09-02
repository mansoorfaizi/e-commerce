from rest_framework import serializers
from ..models import ReturnOrders

class ReturnOrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = ReturnOrders
        fields = '__all__'