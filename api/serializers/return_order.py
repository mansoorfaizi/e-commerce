from rest_framework import serializers
from ..models import return_orders

class ReturnOrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = return_orders
        fields = '__all__'