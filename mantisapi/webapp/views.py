from django.shortcuts import redirect, render
from django.views import View
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponse
from django.contrib import messages
from django.contrib import auth

# Create your views here.


class SignupView(View):
    def get(self, request):
        return render(request, "pages/authentication/signup.html")


class ForgotPassword(View):
    def get(self, request):
        return render(request, "pages/authentication/forgot-password.html")


class LoginView(View):
    def get(self, request):
        return render(request, "pages/authentication/login.html")


class LogoutView(View):
    def post(self, request):
        auth.logout(request)
        messages.success(request, "You have successfully logged out")
        return redirect("login")
