from rest_framework import serializers
from rest_framework import serializers
from .models import User

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'email_or_phone')

class SignInSerializer(serializers.Serializer):
    email_phone = serializers.CharField(required=True)
