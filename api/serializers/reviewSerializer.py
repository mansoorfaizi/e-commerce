from rest_framework import serializers
from api.models.review import Review



class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        user = serializers.StringRelatedField(read_only=True)   
        product = serializers.StringRelatedField(read_only=True)
        
        model = Review
        field = '__all__'
        