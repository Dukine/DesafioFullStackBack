from django.urls import path
from rest_framework_simplejwt import views as jwt_views
from .views import UserView, UserDetailView

urlpatterns = [
    path('login/', jwt_views.TokenObtainPairView.as_view()),
    path('', UserView.as_view()),
    path('<uuid:user_id>/', UserDetailView.as_view())
]