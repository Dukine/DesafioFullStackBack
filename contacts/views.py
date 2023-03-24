from django.shortcuts import render
from rest_framework.views import Response
from rest_framework import generics
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.permissions import IsAuthenticated
from .models import Contact
from .serializers import ContactSerializer
from utils.permissions import ContactOwnerPermissions

class ContactView(generics.ListCreateAPIView):
    authentication_classes= [JWTAuthentication]
    permission_classes = [IsAuthenticated]

    queryset= Contact.objects.all()
    serializer_class= ContactSerializer

    def get(self, request, *args, **kwargs):
        contacts = Contact.objects.filter(user=request.user)

        serializer = self.serializer_class(contacts, many=True)

        return Response(serializer.data)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

class ContactDetailView(generics.RetrieveUpdateDestroyAPIView):
    authentication_classes= [JWTAuthentication]
    permission_classes = [IsAuthenticated, ContactOwnerPermissions]

    queryset= Contact.objects.all()
    serializer_class= ContactSerializer
    lookup_url_kwarg = 'contact_id'