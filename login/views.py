from django.shortcuts import render
from rest_framework.response import Response
from rest_framework import viewsets
from .loginSerializer import LoginSerializer

# Create your views here.
class LoginViewSet(viewsets.ModelViewSet):
    serializer_class = LoginSerializer
    def test(self):
        return Response({
            'teste': 'teste'
        })