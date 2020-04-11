from rest_framework import status, generics
from rest_framework.authtoken.serializers import AuthTokenSerializer
from rest_framework.response import Response
from rest_framework import views
from rest_framework.authtoken.models import Token
from .serializers import UserSerializer
from rest_framework.permissions import IsAuthenticated, AllowAny
from django.core.exceptions import ObjectDoesNotExist


class UserCreateView(generics.CreateAPIView):
    permission_classes = [AllowAny]
    serializer_class = UserSerializer


class LogoutView(generics.DestroyAPIView):
    serializer_class = AuthTokenSerializer

    def get_serializer_context(self):
        response = super().get_serializer_context()
        response['auth_token'] = self.request.user.auth_token
        return response
