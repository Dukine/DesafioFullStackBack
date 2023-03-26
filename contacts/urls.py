from django.urls import path
from rest_framework_simplejwt import views as jwt_views
from .views import ContactView, ContactDetailView

urlpatterns = [
    path('',ContactView.as_view()),
    path('<uuid:contact_id>/', ContactDetailView.as_view())
]