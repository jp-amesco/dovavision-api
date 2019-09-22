from rest_framework import generics
from rest_framework.response import Response
from rest_framework.permissions import AllowAny
from . import models
from .serializers import UserSerializer

class UserList(generics.ListAPIView):
    queryset = models.User.objects.all()
    serializer_class = UserSerializer

class UserCreate(generics.CreateAPIView):
    permission_classes = [AllowAny]
    serializer_class = UserSerializer