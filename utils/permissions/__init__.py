from users.models import User
from contacts.models import Contact
from rest_framework import permissions
from rest_framework.views import Request, View

class OwnerPermissions(permissions.BasePermission):
    def has_object_permission(self, request: Request, view: View, user: User):
        return request.user.is_authenticated and user.email == request.user.email
    
class ContactOwnerPermissions(permissions.BasePermission):
    def has_object_permission(self, request: Request, view: View, contact: Contact):
        return request.user.is_authenticated and contact.user.email == request.user.email