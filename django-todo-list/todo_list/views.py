from rest_framework import status, permissions
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib import messages
from .models import List
from .serializers import ListSerializer, UserSerializer, LoginSerializer

# Home view (List all items or create a new one)
class ListAPIView(ListCreateAPIView):
    queryset = List.objects.all()
    serializer_class = ListSerializer
    permission_classes = [permissions.IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

# Delete item view
class DeleteItemAPIView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def delete(self, request, item_id, format=None):
        item = List.objects.get(pk=item_id)
        item.delete()
        return Response({"message": "Item deleted successfully!"}, status=status.HTTP_204_NO_CONTENT)

# Cross off item view (mark as completed)
class CrossOffItemAPIView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def post(self, request, item_id, format=None):
        item = List.objects.get(pk=item_id)
        item.completed = True
        item.save()
        return Response({"message": "Item marked as completed!"}, status=status.HTTP_200_OK)

# Uncross item view (mark as not completed)
class UncrossItemAPIView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def post(self, request, item_id, format=None):
        item = List.objects.get(pk=item_id)
        item.completed = False
        item.save()
        return Response({"message": "Item marked as not completed!"}, status=status.HTTP_200_OK)

# Edit item view
class EditItemAPIView(RetrieveUpdateDestroyAPIView):
    queryset = List.objects.all()
    serializer_class = ListSerializer
    permission_classes = [permissions.IsAuthenticated]

# Signup view
class SignupAPIView(APIView):
    def post(self, request, *args, **kwargs):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.save()
            login(request, user)  # Log the user in after signup
            return Response({"message": f"Account created successfully! Welcome, {user.username}!"}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# Login view
class LoginAPIView(APIView):
    def post(self, request, *args, **kwargs):
        serializer = LoginSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.validated_data['user']
            login(request, user)
            return Response({"message": "Logged in successfully!"}, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# Logout view
class LogoutAPIView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def post(self, request, *args, **kwargs):
        logout(request)
        return Response({"message": "You have been logged out."}, status=status.HTTP_200_OK)
