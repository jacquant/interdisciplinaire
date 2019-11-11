"""interdisciplinaire URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
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
from django.conf import settings
from django.contrib import admin
from django.urls import path, include, re_path
from drf_yasg import openapi
from drf_yasg.views import get_schema_view
from rest_framework import routers, permissions

from backend.climate_actions.views import index_view, AdaptationActionView

router = routers.DefaultRouter()
schema_view = get_schema_view(
    openapi.Info(
        title="Projet interdisciplinaire",
        default_version="v1",
        description="Api Projet interdisciplinaire",
        terms_of_service="",
        contact=openapi.Contact(email="antoine.jacques@student.unamur.be"),
        license=openapi.License(name="Apache Licence 2.0"),
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
)
router.register("adaptation_action", AdaptationActionView)

urlpatterns = [
    re_path(
        r"^swagger(?P<format>\.json|\.yaml)$",
        schema_view.without_ui(cache_timeout=0),
        name="schema-json",
    ),
    re_path(
        r"^api-doc/$",
        schema_view.with_ui("swagger", cache_timeout=0),
        name="schema-swagger-ui",
    ),
    re_path(
        r"^redoc/$", schema_view.with_ui("redoc", cache_timeout=0), name="schema-redoc"
    ),
    path("", index_view, name="index"),
    path("admin/", admin.site.urls),
    path("api/", include(router.urls)),
]
