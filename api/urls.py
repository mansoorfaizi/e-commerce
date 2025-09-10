from django.urls import path, include
from rest_framework.routers import DefaultRouter
from api.views.category import CategoryViewSet
from api.views.order import OrderViewset, OrderItemViewset

router = DefaultRouter()
router.register(r'categories', CategoryViewSet, basename='category')
router.register(r'orders',OrderViewset , basename='order')
router.register(r'order-items',OrderViewset , basename='orderitem')

urlpatterns = [
    path('', include(router.urls)),
]
