from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import *
from .registration import RegisterUserView
from .authentication import LoginUserView

# 🎯 Routeur DRF pour les ViewSets CRUD
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

# 🌐 URLs de l’application
urlpatterns = [
    path('', include(router.urls)),                                 # Routes CRUD automatiques
    path('stats/', stats_view, name='stats'),                       # Endpoint statistiques
    path('register/', RegisterUserView.as_view(), name='user-register'),  # Inscription utilisateur
    path('login/', LoginUserView.as_view(), name='user-login'),     # Authentification JWT personnalisée
]
