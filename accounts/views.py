from django.shortcuts import render
from rest_framework.permissions import AllowAny
from rest_framework import generics
from . models import *
from . serializer import *



class RegisterViewSet(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = RegisterSerializer
    permission_classes = [AllowAny]


