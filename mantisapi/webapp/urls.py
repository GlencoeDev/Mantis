from .views import *
from django.urls import path
from django.views.decorators.csrf import csrf_exempt

urlpatterns = [
    path("signup", SignupView.as_view(), name="signup"),
    path("login", LoginView.as_view(), name="login"),
    # path('activate', ActivateAccount.as_view(), name="activate-account"),
    path("forgot-password", ForgotPassword.as_view(), name="forgot-password"),
    path("logout", LogoutView.as_view(), name="logout"),
]
