from django.urls import path, include
from rest_framework.routers import DefaultRouter
from api.views.category import CategoryViewSet
from api.views.review import ReviewViewSet

router = DefaultRouter()
router.register(r'categories', CategoryViewSet, basename='category')
router.register(r'reviews', ReviewViewSet, basename='review')


urlpatterns = [
    path('', include(router.urls)),
]
