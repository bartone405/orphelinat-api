from rest_framework import viewsets
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.views import APIView
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework import status
from django.contrib.auth.models import User
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

# ✅ Vue d'authentification login
class LoginUserView(APIView):
    def post(self, request):
        serializer = LoginSerializer(data=request.data)
        if not serializer.is_valid():
            return Response({'error': 'Veuillez fournir username et password'}, status=status.HTTP_400_BAD_REQUEST)

        username = serializer.validated_data.get("username")
        password = serializer.validated_data.get("password")

        try:
            user_obj = UsersTb.objects.get(username=username)
        except UsersTb.DoesNotExist:
            return Response({'error': 'Utilisateur non trouvé'}, status=status.HTTP_404_NOT_FOUND)

        if password == user_obj.user_pswd:
            user = User(username=user_obj.username)
            user.id = user_obj.user_id
            user.is_active = True

            refresh = RefreshToken.for_user(user)
            return Response({
                'refresh': str(refresh),
                'access': str(refresh.access_token),
            }, status=status.HTTP_200_OK)

        return Response({'error': 'Mot de passe incorrect'}, status=status.HTTP_401_UNAUTHORIZED)
