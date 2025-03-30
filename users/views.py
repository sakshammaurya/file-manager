from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from django.contrib.auth.models import User
from .models import UserProfile, Address
from .serializers import UserProfileSerializer, AddressSerializer, UserSerializer

class ProfileView(APIView):
    permission_classes = [IsAuthenticated]  # Restrict to authenticated users

    def get(self, request):
        profile, _ = UserProfile.objects.get_or_create(user=request.user)
        serializer = UserProfileSerializer(profile)
        return Response(serializer.data)

    def post(self, request):
        if not request.user.is_authenticated:
            return Response({'error': 'Authentication required'}, status=status.HTTP_401_UNAUTHORIZED)
        profile, _ = UserProfile.objects.get_or_create(user=request.user)
        if 'username' in request.data:
            request.user.username = request.data['username']
            request.user.save()
        if 'phone_number' in request.data:
            profile.phone_number = request.data['phone_number']
            profile.save()
        if 'addresses' in request.data:
            Address.objects.filter(user=request.user).delete()
            for addr_data in request.data['addresses']:
                Address.objects.create(user=request.user, **addr_data)
        serializer = UserProfileSerializer(profile)
        return Response(serializer.data)

class UserCreateView(APIView):
    def post(self, request):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'status': 'user created'}, status=status.HTTP_201_CREATED)
        return Response({'errors':serializer.errors}, status=status.HTTP_400_BAD_REQUEST)