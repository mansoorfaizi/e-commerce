from rest_framework import status, permissions, viewsets
from rest_framework.response import Response
from knox.models import AuthToken
from django.utils import timezone
from django.core.mail import send_mail
from django.conf import settings
import random
from .models import User
from .serializers import (
    UserSerializer, RegisterSerializer, LoginSerializer,
    ChangePasswordSerializer, ForgotPasswordSerializer, ResetPasswordSerializer,
    VerifyEmailSerializer
)


class RegisterViewSet(viewsets.GenericViewSet):
    permission_classes = [permissions.AllowAny]
    
    def create(self, request):
        serializer = RegisterSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.save()
            
            otp = random.randint(100000, 999999)
            user.otp = otp
            user.save()
            
            send_mail(
                'Email Verification OTP',
                f'Welcome! Your OTP for email verification is: {otp}',
                settings.DEFAULT_FROM_EMAIL,
                [user.email],
                fail_silently=False,
            )
            
            return Response({
                'user': UserSerializer(user).data,
                'message': 'User registered successfully. Verification email sent.'
            }, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class LoginViewSet(viewsets.GenericViewSet):
    permission_classes = [permissions.AllowAny]
    
    def create(self, request):
        serializer = LoginSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.validated_data['user']
            
            if not user.is_verified:
                return Response({
                    'error': 'Email not verified. Please verify your email first.'
                }, status=status.HTTP_400_BAD_REQUEST)
            
            user.last_login = timezone.now()
            user.save()
            token = AuthToken.objects.create(user)[1]
            return Response({
                'user': UserSerializer(user).data,
                'token': token
            })
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class LogoutViewSet(viewsets.GenericViewSet):
    permission_classes = [permissions.IsAuthenticated]
    
    def create(self, request):
        request._auth.delete()
        return Response({'message': 'Logged out successfully'})


class LogoutAllViewSet(viewsets.GenericViewSet):
    permission_classes = [permissions.IsAuthenticated]
    
    def create(self, request):
        request.user.auth_token_set.all().delete()
        return Response({'message': 'Logged out from all devices'})


class ProfileViewSet(viewsets.GenericViewSet):
    permission_classes = [permissions.IsAuthenticated]
    
    def retrieve(self, request, pk=None):
        serializer = UserSerializer(request.user)
        return Response(serializer.data)
    
    def update(self, request, pk=None):
        serializer = UserSerializer(request.user, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ChangePasswordViewSet(viewsets.GenericViewSet):
    permission_classes = [permissions.IsAuthenticated]
    
    def create(self, request):
        serializer = ChangePasswordSerializer(data=request.data, context={'request': request})
        if serializer.is_valid():
            user = request.user
            user.set_password(serializer.validated_data['new_password'])
            user.save()
            user.auth_token_set.all().delete()
            return Response({'message': 'Password changed successfully. Please login again.'})
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ForgotPasswordViewSet(viewsets.GenericViewSet):
    permission_classes = [permissions.AllowAny]
    
    def create(self, request):
        serializer = ForgotPasswordSerializer(data=request.data)
        if serializer.is_valid():
            email = serializer.validated_data['email']
            user = User.objects.get(email=email)
            otp = random.randint(100000, 999999)
            user.otp = otp
            user.save()
            
            send_mail(
                'Password Reset OTP',
                f'Your OTP for password reset is: {otp}',
                settings.DEFAULT_FROM_EMAIL,
                [email],
                fail_silently=False,
            )
            
            return Response({'message': 'OTP sent to your email'})
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ResetPasswordViewSet(viewsets.GenericViewSet):
    permission_classes = [permissions.AllowAny]
    
    def create(self, request):
        serializer = ResetPasswordSerializer(data=request.data)
        if serializer.is_valid():
            email = serializer.validated_data['email']
            otp = serializer.validated_data['otp']
            new_password = serializer.validated_data['new_password']
            
            try:
                user = User.objects.get(email=email, otp=otp)
                user.set_password(new_password)
                user.otp = None
                user.save()
                user.auth_token_set.all().delete()
                return Response({'message': 'Password reset successfully. Please login again.'})
            except User.DoesNotExist:
                return Response({'error': 'Invalid email or OTP'}, status=status.HTTP_400_BAD_REQUEST)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class SendVerificationEmailViewSet(viewsets.GenericViewSet):
    permission_classes = [permissions.AllowAny]
    
    def create(self, request):
        email = request.data.get('email')
        if not email:
            return Response({'error': 'Email is required'}, status=status.HTTP_400_BAD_REQUEST)
        
        try:
            user = User.objects.get(email=email)
            if user.is_verified:
                return Response({'message': 'Email already verified'})
            
            otp = random.randint(100000, 999999)
            user.otp = otp
            user.save()
            
            send_mail(
                'Email Verification OTP',
                f'Your OTP for email verification is: {otp}',
                settings.DEFAULT_FROM_EMAIL,
                [email],
                fail_silently=False,
            )
            
            return Response({'message': 'Verification OTP sent to your email'})
        except User.DoesNotExist:
            return Response({'error': 'User with this email does not exist'}, status=status.HTTP_400_BAD_REQUEST)


class VerifyEmailViewSet(viewsets.GenericViewSet):
    permission_classes = [permissions.AllowAny]
    
    def create(self, request):
        serializer = VerifyEmailSerializer(data=request.data)
        if serializer.is_valid():
            email = serializer.validated_data['email']
            otp = serializer.validated_data['otp']
            
            try:
                user = User.objects.get(email=email, otp=otp)
                user.is_verified = True
                user.otp = None
                user.save()
                return Response({'message': 'Email verified successfully'})
            except User.DoesNotExist:
                return Response({'error': 'Invalid email or OTP'}, status=status.HTTP_400_BAD_REQUEST)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
