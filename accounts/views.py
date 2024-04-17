from django.shortcuts import render
from rest_framework.response import Response
from .models import CustomUser
from rest_framework import generics, status
from rest_framework_simplejwt.tokens import RefreshToken
from .serializers import *
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated


# Create your views here.


class RegistrationView(generics.CreateAPIView):
    serializer_class = RegisterSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        response_data = serializer.create(validated_data=serializer.validated_data)

        return Response(response_data, status=status.HTTP_201_CREATED)


class LoginAPIView(generics.GenericAPIView):
    serializer_class = LoginSerializer
    
    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    


class LogoutAPIView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        try:
            refresh_token = request.data['refresh_token']

            token = RefreshToken(refresh_token)
            token.blacklist()


            return Response({"detail": "Successfully logged out."})

        except Exception as e:
            return Response({"detail": "Invalid or missing refresh token."}, status=400)