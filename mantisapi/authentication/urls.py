from .views import *
from django.urls import path
from rest_framework_simplejwt.views import TokenRefreshView
from django.views.decorators.csrf import csrf_exempt

urlpatterns = [
    path("signup", RegisterView.as_view(), name="signup"),
    path("login", csrf_exempt(LoginApiView.as_view()), name="login"),
    path("activate", ActivateAccount.as_view(), name="activate-account"),
    path("forgot-password", ForgotPasswordView.as_view(), name="forgot-password"),
    # This uses the JWT Package to enable users to generate access tokens when logged in by using their current refresh token
    path("token/refresh", TokenRefreshView.as_view(), name="token_refresh"),
    path(
        "password-reset-complete",
        SetNewPasswordAPIView.as_view(),
        name="password-reset-complete",
    ),
    path(
        "password-reset/<uidb64>/<token>/",
        PasswordTokenCheckAPI.as_view(),
        name="password-reset-confirm",
    ),  # This url coiolects the encoded user information and token sent to their email for resseting password
]
