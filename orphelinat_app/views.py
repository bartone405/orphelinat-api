from rest_framework import viewsets
from django_filters.rest_framework import DjangoFilterBackend
import django_filters

from .models import (
    UsersTb, OrphelinsTb, AdoptionsTb, AdoptantsTb, DocumentsTb,
    DonatorsTb, GiftsTb, MedicalVisitsTb, EducationTb,
    CountryTb, StatusTb, RolesTb, SexTb,
    ActionsTb, MessagesTb, OrphelinatsTb
)

from .serializers import (
    UsersTbSerializer, OrphelinsTbSerializer, AdoptionsTbSerializer, AdoptantsTbSerializer,
    DocumentsTbSerializer, DonatorsTbSerializer, GiftsTbSerializer, MedicalVisitsTbSerializer,
    EducationTbSerializer, CountryTbSerializer, StatusTbSerializer, RolesTbSerializer,
    SexTbSerializer, ActionsTbSerializer, MessagesTbSerializer, OrphelinatsTbSerializer
)

from rest_framework.decorators import api_view
from rest_framework.response import Response

# Filtres personnalisés pour Orphelins
class OrphelinFilter(django_filters.FilterSet):
    class Meta:
        model = OrphelinsTb
        fields = {
            'orphelin_fname': ['icontains'],
            'orphelin_dob': ['year__lte'],
            'orphelin_lname': ['icontains'],
        }

class UsersTbViewSet(viewsets.ModelViewSet):
    queryset = UsersTb.objects.all()
    serializer_class = UsersTbSerializer

class OrphelinsTbViewSet(viewsets.ModelViewSet):
    queryset = OrphelinsTb.objects.select_related('orphelinat', 'sex', 'country', 'status').all()
    serializer_class = OrphelinsTbSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_class = OrphelinFilter

class AdoptionsTbViewSet(viewsets.ModelViewSet):
    queryset = AdoptionsTb.objects.select_related('orphelin', 'adoptant', 'status').all()
    serializer_class = AdoptionsTbSerializer

class AdoptantsTbViewSet(viewsets.ModelViewSet):
    queryset = AdoptantsTb.objects.select_related('sex', 'country', 'status').all()
    serializer_class = AdoptantsTbSerializer

class DocumentsTbViewSet(viewsets.ModelViewSet):
    queryset = DocumentsTb.objects.select_related('orphelin').all()
    serializer_class = DocumentsTbSerializer

class DonatorsTbViewSet(viewsets.ModelViewSet):
    queryset = DonatorsTb.objects.select_related('sex', 'country', 'status').all()
    serializer_class = DonatorsTbSerializer

class GiftsTbViewSet(viewsets.ModelViewSet):
    queryset = GiftsTb.objects.select_related('donator', 'status').all()
    serializer_class = GiftsTbSerializer

class MedicalVisitsTbViewSet(viewsets.ModelViewSet):
    queryset = MedicalVisitsTb.objects.select_related('orphelin').all()
    serializer_class = MedicalVisitsTbSerializer

class EducationTbViewSet(viewsets.ModelViewSet):
    queryset = EducationTb.objects.select_related('orphelin').all()
    serializer_class = EducationTbSerializer

class CountryTbViewSet(viewsets.ModelViewSet):
    queryset = CountryTb.objects.all()
    serializer_class = CountryTbSerializer

class StatusTbViewSet(viewsets.ModelViewSet):
    queryset = StatusTb.objects.all()
    serializer_class = StatusTbSerializer

class RolesTbViewSet(viewsets.ModelViewSet):
    queryset = RolesTb.objects.all()
    serializer_class = RolesTbSerializer

class SexTbViewSet(viewsets.ModelViewSet):
    queryset = SexTb.objects.all()
    serializer_class = SexTbSerializer

class ActionsTbViewSet(viewsets.ModelViewSet):
    queryset = ActionsTb.objects.all()
    serializer_class = ActionsTbSerializer

class MessagesTbViewSet(viewsets.ModelViewSet):
    queryset = MessagesTb.objects.select_related('sender', 'receiver').all()
    serializer_class = MessagesTbSerializer

class OrphelinatsTbViewSet(viewsets.ModelViewSet):
    queryset = OrphelinatsTb.objects.all()
    serializer_class = OrphelinatsTbSerializer

# Vue statistiques sans restriction
@api_view(['GET'])
def stats_view(request):
    data = {
        "total_utilisateurs": UsersTb.objects.count(),
        "total_orphelins": OrphelinsTb.objects.count(),
        "total_adoptions": AdoptionsTb.objects.count(),
    }