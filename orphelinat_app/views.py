from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
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

from .permissions import IsAdminRole  # ton permission custom admin
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
    permission_classes = [IsAuthenticated, IsAdminRole]

class OrphelinsTbViewSet(viewsets.ModelViewSet):
    queryset = OrphelinsTb.objects.select_related('orphelinat', 'sex', 'country', 'status').all()
    serializer_class = OrphelinsTbSerializer
    permission_classes = [IsAuthenticated]
    filter_backends = [DjangoFilterBackend]
    filterset_class = OrphelinFilter

class AdoptionsTbViewSet(viewsets.ModelViewSet):
    queryset = AdoptionsTb.objects.select_related('orphelin', 'adoptant', 'status').all()
    serializer_class = AdoptionsTbSerializer
    permission_classes = [IsAuthenticated]

class AdoptantsTbViewSet(viewsets.ModelViewSet):
    queryset = AdoptantsTb.objects.select_related('sex', 'country', 'status').all()
    serializer_class = AdoptantsTbSerializer
    permission_classes = [IsAuthenticated]

class DocumentsTbViewSet(viewsets.ModelViewSet):
    queryset = DocumentsTb.objects.select_related('orphelin').all()
    serializer_class = DocumentsTbSerializer
    permission_classes = [IsAuthenticated]

class DonatorsTbViewSet(viewsets.ModelViewSet):
    queryset = DonatorsTb.objects.select_related('sex', 'country', 'status').all()
    serializer_class = DonatorsTbSerializer
    permission_classes = [IsAuthenticated]

class GiftsTbViewSet(viewsets.ModelViewSet):
    queryset = GiftsTb.objects.select_related('donator', 'status').all()
    serializer_class = GiftsTbSerializer
    permission_classes = [IsAuthenticated]

class MedicalVisitsTbViewSet(viewsets.ModelViewSet):
    queryset = MedicalVisitsTb.objects.select_related('orphelin').all()
    serializer_class = MedicalVisitsTbSerializer
    permission_classes = [IsAuthenticated]

class EducationTbViewSet(viewsets.ModelViewSet):
    queryset = EducationTb.objects.select_related('orphelin').all()
    serializer_class = EducationTbSerializer
    permission_classes = [IsAuthenticated]

class CountryTbViewSet(viewsets.ModelViewSet):
    queryset = CountryTb.objects.all()
    serializer_class = CountryTbSerializer
    permission_classes = [IsAuthenticated]

class StatusTbViewSet(viewsets.ModelViewSet):
    queryset = StatusTb.objects.all()
    serializer_class = StatusTbSerializer
    permission_classes = [IsAuthenticated]

class RolesTbViewSet(viewsets.ModelViewSet):
    queryset = RolesTb.objects.all()
    serializer_class = RolesTbSerializer
    permission_classes = [IsAuthenticated]

class SexTbViewSet(viewsets.ModelViewSet):
    queryset = SexTb.objects.all()
    serializer_class = SexTbSerializer
    permission_classes = [IsAuthenticated]

class ActionsTbViewSet(viewsets.ModelViewSet):
    queryset = ActionsTb.objects.all()
    serializer_class = ActionsTbSerializer
    permission_classes = [IsAuthenticated]

class MessagesTbViewSet(viewsets.ModelViewSet):
    queryset = MessagesTb.objects.select_related('sender', 'receiver').all()
    serializer_class = MessagesTbSerializer
    permission_classes = [IsAuthenticated]

class OrphelinatsTbViewSet(viewsets.ModelViewSet):
    queryset = OrphelinatsTb.objects.all()
    serializer_class = OrphelinatsTbSerializer
    permission_classes = [IsAuthenticated]

# ✅ Vue statistique
@api_view(['GET'])
def stats_view(request):
    data = {
        "total_utilisateurs": UsersTb.objects.count(),
        "total_orphelins": OrphelinsTb.objects.count(),
        "total_adoptions": AdoptionsTb.objects.count(),
        "total_adoptants": AdoptantsTb.objects.count(),
        "total_documents": DocumentsTb.objects.count(),
        "total_donateurs": DonatorsTb.objects.count(),
        "total_dons": GiftsTb.objects.count(),
        "total_visites_médicales": MedicalVisitsTb.objects.count(),
        "total_éducation": EducationTb.objects.count(),
        "total_actions": ActionsTb.objects.count(),
        "total_messages": MessagesTb.objects.count(),
        "total_orphelinats": OrphelinatsTb.objects.count(),
    }
    return Response(data)
