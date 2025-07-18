from django.urls import path, include
from rest_framework.routers import DefaultRouter
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

urlpatterns = [
    path('', include(router.urls)),
    path('stats/', stats_view, name='stats'),
    path('login/', LoginUserView.as_view(), name='login'),
    path('register/', RegisterUserView.as_view(), name='register'),
]
