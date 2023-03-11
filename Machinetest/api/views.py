from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from .serializers import SignInSerializer
import random
from django.core.cache import cache
from django.utils import timezone
from django.views.generic import TemplateView
from rest_framework import generics
from .models import User
from .serializers import UserSerializer

class SignInView(APIView):
    def post(self, request, format=None):
        serializer = SignInSerializer(data=request.data)
        if serializer.is_valid():
            email_phone = serializer.validated_data['email_phone']
            # Redirect to OTP page passing email/phone parameter
            return Response({'status': 'success', 'email_phone': email_phone}, status=status.HTTP_200_OK)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)



class OTPView(APIView):
    def post(self, request, format=None):
        email_phone = request.data.get('email_phone')
        if not email_phone:
            return Response({'error': 'email/phone parameter is required'}, status=status.HTTP_400_BAD_REQUEST)
        otp = str(random.randint(10000, 99999))
        cache_key = f'otp:{email_phone}'
        cache.set(cache_key, otp, timeout=300)
        # Return the OTP to the user
        return Response({'status': 'success', 'email_phone': email_phone}, status=status.HTTP_200_OK)



class UserListView(TemplateView):
    template_name = 'dashboard.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['users'] = User.objects.all()
        return context
