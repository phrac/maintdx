from django.shortcuts import render
from django.contrib.auth.models import User
from rest_framework import viewsets
from maintdx.users.serializers import UserSerializer

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all().order_by('username');
    serializer_class = UserSerializer
