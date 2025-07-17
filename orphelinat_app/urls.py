from django.urls import path, include, re_path
from rest_framework.routers import DefaultRouter

from .views import (
    UsersTbViewSet, OrphelinsTbViewSet, AdoptionsTbViewSet, AdoptantsTbViewSet,
    DocumentsTbViewSet, DonatorsTbViewSet, GiftsTbViewSet, MedicalVisitsTbViewSet,
    EducationTbViewSet, CountryTbViewSet, StatusTbViewSet, RolesTbViewSet,
    SexTbViewSet, ActionsTbViewSet, MessagesTbViewSet, OrphelinatsTbViewSet,
    stats_view
)
from .registration import RegisterUserView
from .authentication import LoginUserView

from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

schema_view = get_schema_view(
    openapi.Info(
        title="Orphelinat API",
        default_version='v1',
        description="Documentation publique de l'API REST de l'orphelinat",
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
    url="https://orphelinat-api.onrender.com/api"  # ← Mets ici l’URL publique de ton backend Render
)

router = DefaultRouter()
router.register(r'users', UsersTbViewSet)
router.register(r'orphelins', OrphelinsTbViewSet)
router.register(r'adoptions', AdoptionsTbViewSet)
router.register(r'adoptants', AdoptantsTbViewSet)
router.register(r'documents', DocumentsTbViewSet)
router.register(r'donators', DonatorsTbViewSet)
router.register(r'gifts', GiftsTbViewSet)
router.register(r'visites', MedicalVisitsTbViewSet)
router.register(r'education', EducationTbViewSet)
router.register(r'countries', CountryTbViewSet)
router.register(r'status', StatusTbViewSet)
router.register(r'roles', RolesTbViewSet)
router.register(r'sex', SexTbViewSet)
router.register(r'actions', ActionsTbViewSet)
router.register(r'messages', MessagesTbViewSet)
router.register(r'orphelinats', OrphelinatsTbViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('stats/', stats_view, name='stats'),
    path('register/', RegisterUserView.as_view(), name='user-register'),
    path('login/', LoginUserView.as_view(), name='user-login'),

    # Swagger & Redoc
    re_path(r'^swagger(?P<format>\.json|\.yaml)$', schema_view.without_ui(cache_timeout=0), name='schema-json'),
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
]
