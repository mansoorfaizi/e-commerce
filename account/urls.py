from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views

router = DefaultRouter()
router.register(r'register', views.RegisterViewSet, basename='register')
router.register(r'login', views.LoginViewSet, basename='login')
router.register(r'logout', views.LogoutViewSet, basename='logout')
router.register(r'logout-all', views.LogoutAllViewSet, basename='logout-all')
router.register(r'profile', views.ProfileViewSet, basename='profile')
router.register(r'change-password', views.ChangePasswordViewSet, basename='change-password')
router.register(r'forgot-password', views.ForgotPasswordViewSet, basename='forgot-password')
router.register(r'reset-password', views.ResetPasswordViewSet, basename='reset-password')
router.register(r'send-verification-email', views.SendVerificationEmailViewSet, basename='send-verification-email')
router.register(r'verify-email', views.VerifyEmailViewSet, basename='verify-email')

urlpatterns = [
    path('', include(router.urls)),
]