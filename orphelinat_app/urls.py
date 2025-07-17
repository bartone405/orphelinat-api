from django.urls import path, include, re_path
from rest_framework.routers import DefaultRouter
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

from django.http import JsonResponse

def test_view(request):
    return JsonResponse({"message": "Test OK"})


from .views import (
    UsersTbViewSet, OrphelinsTbViewSet, AdoptionsTbViewSet, AdoptantsTbViewSet,
    DocumentsTbViewSet, DonatorsTbViewSet, GiftsTbViewSet, MedicalVisitsTbViewSet,
    EducationTbViewSet, CountryTbViewSet, StatusTbViewSet, RolesTbViewSet,
    SexTbViewSet, ActionsTbViewSet, MessagesTbViewSet, OrphelinatsTbViewSet,
    stats_view, LoginUserView, RegisterUserView
)

router = DefaultRouter()
router.register(r'users', UsersTbViewSet)
router.register(r'orphelins', OrphelinsTbViewSet)
router.register(r'adoptions', AdoptionsTbViewSet)
router.register(r'adoptants', AdoptantsTbViewSet)
router.register(r'documents', DocumentsTbViewSet)
router.register(r'donateurs', DonatorsTbViewSet)
router.register(r'gifts', GiftsTbViewSet)
router.register(r'medical-visits', MedicalVisitsTbViewSet)
router.register(r'education', EducationTbViewSet)
router.register(r'countries', CountryTbViewSet)
router.register(r'status', StatusTbViewSet)
router.register(r'roles', RolesTbViewSet)
router.register(r'sexes', SexTbViewSet)
router.register(r'actions', ActionsTbViewSet)
router.register(r'messages', MessagesTbViewSet)
router.register(r'orphelinats', OrphelinatsTbViewSet)

schema_view = get_schema_view(
    openapi.Info(
        title="API Orphelinat",
        default_version='v1',
        description="Documentation de l'API REST pour l’orphelinat",
    ),
    public=True,
    permission_classes=[permissions.AllowAny],
)

urlpatterns = [
    path('test/', test_view),
    path('', include(router.urls)),
    path('stats/', stats_view, name='stats'),
    path('login/', LoginUserView.as_view(), name='login'),
    path('register/', RegisterUserView.as_view(), name='register'),

    # Swagger documentation routes (JSON, YAML, Swagger UI, Redoc)
    re_path(r'^swagger(?P<format>\.json|\.yaml)$', schema_view.without_ui(cache_timeout=0), name='schema-json'),
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
]
