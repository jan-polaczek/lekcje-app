from django.http import JsonResponse
from rest_framework import status, generics
from rest_framework.authtoken.serializers import AuthTokenSerializer
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.response import Response
from rest_framework import views
from rest_framework.authtoken.models import Token
from .serializers import UserSerializer
from rest_framework.permissions import IsAuthenticated, AllowAny
from django.core.exceptions import ObjectDoesNotExist
from .models import *


class UserCreateView(generics.CreateAPIView):
    permission_classes = [AllowAny]
    serializer_class = UserSerializer


class LogoutView(generics.DestroyAPIView):
    serializer_class = AuthTokenSerializer

    def get_serializer_context(self):
        response = super().get_serializer_context()
        response['auth_token'] = self.request.user.auth_token
        return response


class AccountsView(generics.ListAPIView):
    serializer_class = UserSerializer
    queryset = User.objects.all()


class LoginView(ObtainAuthToken):
    permission_classes = [AllowAny]

    def post(self, request, *args, **kwargs):
        login_response = super().post(request, *args, **kwargs)
        print(login_response.data)
        user = User.objects.get(auth_token=login_response.data['token'])
        serializer = UserSerializer(instance=user)
        response = serializer.data
        response['token'] = login_response.data['token']
        return Response(response)

