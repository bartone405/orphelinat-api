from rest_framework import viewsets
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django_filters.rest_framework import DjangoFilterBackend
from .models import *
from .serializers import *

import django_filters

# 🔍 Filtres personnalisés pour les orphelins
class OrphelinFilter(django_filters.FilterSet):
    class Meta:
        model = OrphelinsTb
        fields = {
            'orphelin_fname': ['icontains'],
            'orphelin_dob': ['year__lte'],
        }

# 🔄 ViewSets pour chaque modèle
class UsersTbViewSet(viewsets.ModelViewSet):
    queryset = UsersTb.objects.all()
    serializer_class = UsersTbSerializer

class OrphelinsTbViewSet(viewsets.ModelViewSet):
    queryset = OrphelinsTb.objects.select_related('orphelinat', 'sex').all()
    serializer_class = OrphelinsTbSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_class = OrphelinFilter

class AdoptionsTbViewSet(viewsets.ModelViewSet):
    queryset = AdoptionsTb.objects.select_related('orphelin', 'adoptant').all()
    serializer_class = AdoptionsTbSerializer

class AdoptantsTbViewSet(viewsets.ModelViewSet):
    queryset = AdoptantsTb.objects.all()
    serializer_class = AdoptantsTbSerializer

class DocumentsTbViewSet(viewsets.ModelViewSet):
    queryset = DocumentsTb.objects.all()
    serializer_class = DocumentsTbSerializer

class DonatorsTbViewSet(viewsets.ModelViewSet):
    queryset = DonatorsTb.objects.all()
    serializer_class = DonatorsTbSerializer

class GiftsTbViewSet(viewsets.ModelViewSet):
    queryset = GiftsTb.objects.all()
    serializer_class = GiftsTbSerializer

class MedicalVisitsTbViewSet(viewsets.ModelViewSet):
    queryset = MedicalVisitsTb.objects.all()
    serializer_class = MedicalVisitsTbSerializer

class EducationTbViewSet(viewsets.ModelViewSet):
    queryset = EducationTb.objects.all()
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
    queryset = MessagesTb.objects.all()
    serializer_class = MessagesTbSerializer

class OrphelinatsTbViewSet(viewsets.ModelViewSet):
    queryset = OrphelinatsTb.objects.all()
    serializer_class = OrphelinatsTbSerializer

# 🔢 Statistiques globales (nombre total)
@api_view(['GET'])
def stats_view(request):
    return Response({
        'total_orphelins': OrphelinsTb.objects.count(),
        'total_adoptions': AdoptionsTb.objects.count(),
    })
