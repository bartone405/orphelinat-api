# orphelinat_app/urls.py

from django.urls import path, include
from rest_framework.routers import DefaultRouter
from orphelinat_app import views

router = DefaultRouter()
router.register(r'users', views.UsersTbViewSet)
router.register(r'orphelins', views.OrphelinsTbViewSet)
router.register(r'adoptions', views.AdoptionsTbViewSet)
router.register(r'adoptants', views.AdoptantsTbViewSet)
router.register(r'documents', views.DocumentsTbViewSet)
router.register(r'donators', views.DonatorsTbViewSet)
router.register(r'gifts', views.GiftsTbViewSet)
router.register(r'visites-medicales', views.MedicalVisitsTbViewSet)
router.register(r'educations', views.EducationTbViewSet)
router.register(r'pays', views.CountryTbViewSet)
router.register(r'status', views.StatusTbViewSet)
router.register(r'roles', views.RolesTbViewSet)
router.register(r'sexes', views.SexTbViewSet)
router.register(r'actions', views.ActionsTbViewSet)
router.register(r'messages', views.MessagesTbViewSet)
router.register(r'orphelinats', views.OrphelinatsTbViewSet)

urlpatterns = [
    path('', include(router.urls)),

    # Routes personnalisées
    path('auth/login/', views.LoginUserView.as_view(), name='login'),
    path('auth/register/', views.RegisterUserView.as_view(), name='register'),
    path('stats/', views.stats_view, name='stats'),
]
