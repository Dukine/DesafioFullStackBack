from django.shortcuts import render
from rest_framework import generics
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.permissions import AllowAny, IsAuthenticated
from .models import User
from .serializers import UserSerializer
from utils.permissions import OwnerPermissions


class UserView(generics.ListCreateAPIView):
    authentication_classes= [JWTAuthentication]
    queryset= User.objects.all()
    serializer_class= UserSerializer

    def get_permissions(self):
        if self.request.method == "POST":
            return [AllowAny()]
        return [IsAuthenticated()]

    def get_queryset(self):
        if self.request.method == "POST":
            return User.objects.all()
        return User.objects.filter(id= self.request.user.id)

class UserDetailView(generics.RetrieveUpdateDestroyAPIView):
    authentication_classes= [JWTAuthentication]
    permission_classes = [OwnerPermissions]

    queryset= User.objects.all()
    serializer_class= UserSerializer
    lookup_url_kwarg = 'user_id'
