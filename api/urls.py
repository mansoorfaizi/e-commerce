from django.urls import path, include
from rest_framework.routers import DefaultRouter
from api.views.category import CategoryViewSet
from api.views.order import OrderViewset, OrderItemViewset
from api.views.payment import PaymentViewSet
from api.views.shipping_address import ShippingAdressViewset
from api.views.product import ProductViewSet

router = DefaultRouter()
router.register(r'products', ProductViewSet, basename='products')
router.register(r'categories', CategoryViewSet, basename='category')
router.register(r'orders',OrderViewset , basename='order')
router.register(r'order-items',OrderItemViewset , basename='orderitem')
router.register(r'payment', PaymentViewSet , basename='payment')
router.register(r'shipping-address', ShippingAdressViewset , basename='shippingadress')

urlpatterns = [
    path('', include(router.urls)),
]
