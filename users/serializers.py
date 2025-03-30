from rest_framework import serializers
from django.contrib.auth.models import User
from .models import UserProfile, Address

class AddressSerializer(serializers.ModelSerializer):
    class Meta:
        model = Address
        fields = ['id', 'address', 'is_primary']

class UserProfileSerializer(serializers.ModelSerializer):
    addresses = AddressSerializer(many=True, read_only=True)
    username = serializers.CharField(source='user.username', read_only=True)  # Read-only

    class Meta:
        model = UserProfile
        fields = ['username', 'phone_number', 'addresses']
        extra_kwargs = {
            'phone_number': {'required': False, 'allow_blank': True},
        }

class UserSerializer(serializers.ModelSerializer):
    profile = UserProfileSerializer()

    class Meta:
        model = User
        fields = ['username', 'email', 'password', 'profile']
        extra_kwargs = {
            'password': {'write_only': True},
            'email': {'required': False, 'allow_blank': True},
        }

    def create(self, validated_data):
        profile_data = validated_data.pop('profile', {})
        user = User.objects.create_user(**validated_data)
        UserProfile.objects.create(user=user, **profile_data)
        return user