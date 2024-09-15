from django.urls import path, include

from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

from .views import (
    RegisterView,
    LoginAdminView,
    LoginView,
)

urlpatterns = [
    path("register/", RegisterView.as_view(), name="register"),
    path("login-admin/", LoginAdminView.as_view(), name="login-admin"),
    path("login/", LoginView.as_view(), name="login"),
]
