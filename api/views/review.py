from rest_framework import viewsets
from api.models.review import Review
from api.serializers.review import ReviewSerializer


class ReviewViewSet(viewsets.ModelViewSet):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer
    
    
    