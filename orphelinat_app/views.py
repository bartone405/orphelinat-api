from rest_framework import viewsets, status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework_simplejwt.tokens import RefreshToken
from django.contrib.auth.hashers import check_password, make_password

from orphelinat_app.models import (
    UsersTb, OrphelinsTb, AdoptionsTb, AdoptantsTb, DocumentsTb, DonatorsTb,
    GiftsTb, MedicalVisitsTb, EducationTb, CountryTb, StatusTb, RolesTb,
    SexTb, ActionsTb, MessagesTb, OrphelinatsTb
)

from orphelinat_app.serializers import (
    UsersTbSerializer, OrphelinsTbSerializer, AdoptionsTbSerializer,
    AdoptantsTbSerializer, DocumentsTbSerializer, DonatorsTbSerializer,
    GiftsTbSerializer, MedicalVisitsTbSerializer, EducationTbSerializer,
    CountryTbSerializer, StatusTbSerializer, RolesTbSerializer,
    SexTbSerializer, ActionsTbSerializer, MessagesTbSerializer,
    OrphelinatsTbSerializer
)

# ============================
# ViewSets API REST classiques
# ============================

class UsersTbViewSet(viewsets.ModelViewSet):
    queryset = UsersTb.objects.all()
    serializer_class = UsersTbSerializer

class OrphelinsTbViewSet(viewsets.ModelViewSet):
    queryset = OrphelinsTb.objects.all()
    serializer_class = OrphelinsTbSerializer

class AdoptionsTbViewSet(viewsets.ModelViewSet):
    queryset = AdoptionsTb.objects.all()
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

# ============================
# Vue personnalisée : statistiques
# ============================

@api_view(['GET'])
def stats_view(request):
    orphelins_count = OrphelinsTb.objects.count()
    adoptions_count = AdoptionsTb.objects.count()
    users_count = UsersTb.objects.count()
    return Response({
        "total_orphelins": orphelins_count,
        "total_adoptions": adoptions_count,
        "total_utilisateurs": users_count
    })

# ============================
# Vue personnalisée : Login utilisateur
# ============================

class LoginUserView(APIView):
    def post(self, request):
        username = request.data.get("username")
        password = request.data.get("password")

        try:
            user = UsersTb.objects.get(username=username)
            if check_password(password, user.user_pswd):
                refresh = RefreshToken.for_user(user)
                return Response({
                    "refresh": str(refresh),
                    "access": str(refresh.access_token),
                    "user_id": user.id,
                    "username": user.username,
                    "role_id": user.role_id
                })
            else:
                return Response({"error": "Mot de passe incorrect"}, status=401)
        except UsersTb.DoesNotExist:
            return Response({"error": "Utilisateur non trouvé"}, status=404)

# ============================
# Vue personnalisée : Enregistrement utilisateur
# ============================

class RegisterUserView(APIView):
    def post(self, request):
        data = request.data.copy()
        data["user_pswd"] = make_password(data["user_pswd"])

        serializer = UsersTbSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)
