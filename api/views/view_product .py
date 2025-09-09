from rest_framework import viewsets
from api.models.product import Product, ProductImage
from api.serializers.product_image_serializers import ProductSerializer, ProductImageSerializer

class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer


class ProductImageViewSet(viewsets.ModelViewSet):
    queryset = ProductImage.objects.all()
    serializer_class = ProductImageSerializer
