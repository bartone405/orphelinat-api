"""
URL configuration for orphelinat_project project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
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
from django.urls import path, include, re_path
from rest_framework_simplejwt.views import TokenRefreshView
from orphelinat_app.swagger import schema_view

# Routes API (pas de format_suffix_patterns ici !)
api_urlpatterns = [
    path('api/', include('orphelinat_app.urls')),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]

urlpatterns = [
    path('admin/', admin.site.urls),

    # Routes API directement incluses sans format_suffix_patterns
    *api_urlpatterns,

  re_path(r'^swagger(?P<file_format>\.json|\.yaml)$', schema_view.without_ui(cache_timeout=0), name='schema-json'),



    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
]

