from django.urls import path, include
from rest_framework.routers import DefaultRouter
from api.views.category import CategoryViewSet

from django.urls import path, include
from rest_framework.routers import DefaultRouter
from api.views.payment import PaymentViewSet  # import from payment.py

router = DefaultRouter()
router.register(r'payment', PaymentViewSet , basename='payment')

urlpatterns = [
    path('', include(router.urls)),
]

router = DefaultRouter()
router.register(r'categories', CategoryViewSet, basename='category')

urlpatterns = [
    path('', include(router.urls)),
]
