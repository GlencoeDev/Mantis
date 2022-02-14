"""mantisapi URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.urls import include, path, re_path

# WHEN DEPLOYED CHANGE TO PROD
from mantisapi.settings.dev import *
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from django.conf.urls import handler400, handler403, handler404, handler500

schema_view = get_schema_view(
    openapi.Info(
        title="Glencoe Software Canada: Mantis API",
        default_version="v1.0.0",
        description="Management Web Application with Dynamic Functionality",
        terms_of_service="https://mantis.glencoe.ca/terms-of-service",
        contact=openapi.Contact(email="mantis@glencoe.ca"),
        license=openapi.License(name="GNU General Public License v3.0"),
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
)

urlpatterns = [
    path("auth/", include("authentication.urls")),
    path(
        "api/",
        schema_view.with_ui("swagger", cache_timeout=0),
        name="schema-swagger-ui",
    ),
    path("", include("webapp.urls")),
]


handler400 = "helpers.views.handleError400"
handler403 = "helpers.views.handleError403"
handler404 = "helpers.views.handleError404"
handler500 = "helpers.views.handleError500"


if ADMIN_ENABLED:
    urlpatterns += [path("admin/", admin.site.urls)]
