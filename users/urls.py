from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

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

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
