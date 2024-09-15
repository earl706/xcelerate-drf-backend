from .models import User
from .serializers import (
    UserSerializer,
    RegisterSerializer,
    LoginSerializer,
    PasswordSerializer,
)

from django.shortcuts import render
from django.utils import timezone

from rest_framework import generics, permissions, status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.permissions import AllowAny, IsAuthenticated, IsAdminUser
from rest_framework.authentication import TokenAuthentication
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework_simplejwt.tokens import RefreshToken, AccessToken

from django.contrib.auth import authenticate, login, hashers


# Create your views here.
class RegisterView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = RegisterSerializer
    permission_classes = [IsAdminUser]
    authentication_classes = [JWTAuthentication]

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            self.perform_create(serializer)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class LoginAdminView(APIView):
    permission_classes = [AllowAny]
    authentication_classes = [TokenAuthentication]
    serializer_class = LoginSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = authenticate(
            request,
            full_name=serializer.validated_data["full_name"],
            password=serializer.validated_data["password"],
        )
        if user.is_staff and user.is_superuser:
            refresh = RefreshToken.for_user(user)
            access_token = str(refresh.access_token)
            refresh_token = str(refresh)

            login(request, user)
            return Response(
                {"refresh": refresh_token, "access": access_token}, status=200
            )
        return Response({"error": "Invalid Credentials"}, status=400)


class LoginView(APIView):
    permission_classes = [AllowAny]
    authentication_classes = [TokenAuthentication]
    serializer_class = LoginSerializer

    def post(self, request, *args, **kwargs):
        try:
            serializer = self.serializer_class(data=request.data)
            serializer.is_valid(raise_exception=True)
            user = authenticate(
                request,
                full_name=serializer.validated_data["full_name"],
                password=serializer.validated_data["password"],
            )
            if user:
                refresh = RefreshToken.for_user(user)
                access_token = str(refresh.access_token)
                refresh_token = str(refresh)
                user_detail = User.objects.get(full_name=request.data["full_name"])
                login(request, user)
                return Response(
                    {
                        "access": access_token,
                        "refresh": refresh_token,
                        "user_id": user_detail.id,
                    },
                    status=200,
                )
            print(serializer.errors)
            return Response({"error": "Invalid Credentials"}, status=400)
        except ValueError as e:
            print(e)
            return Response({"error": e}, status=400)
