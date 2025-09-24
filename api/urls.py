from django.urls import path, include
from rest_framework.routers import DefaultRouter
from rest_framework_nested import routers

from api.views.category import CategoryViewSet
from api.views.order import OrderViewset, OrderItemViewset
from api.views.payment import PaymentViewSet
from api.views.shipping_address import ShippingAdressViewset
from api.views.support_chat import SupportChatViewSet, ConversationViewSet

router = DefaultRouter()
router.register(r'categories', CategoryViewSet, basename='category')
router.register(r'orders', OrderViewset, basename='order')
router.register(r'order-items', OrderItemViewset, basename='orderitem')
router.register(r'payments', PaymentViewSet, basename='payment')
router.register(r'shipping-addresses', ShippingAdressViewset, basename='shippingaddress')
router.register(r'support-chats', SupportChatViewSet, basename='supportchat')
router.register(r'conversations', ConversationViewSet, basename='conversation')  # direct access

# Nested router for conversations under support-chats
support_chat_router = routers.NestedSimpleRouter(router, r'support-chats', lookup='support_chat')
support_chat_router.register(r'conversations', ConversationViewSet, basename='supportchat-conversations')

urlpatterns = [
    path('', include(router.urls)),
    path('', include(support_chat_router.urls)),
]
