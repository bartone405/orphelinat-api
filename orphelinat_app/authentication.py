from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.contrib.auth.hashers import check_password
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework.permissions import AllowAny
from .models import UsersTb

class LoginUserView(APIView):
    permission_classes = [AllowAny]  # Permet l'accès sans authentification

    def post(self, request):
        username = request.data.get("username")
        password = request.data.get("password")

        try:
            user = UsersTb.objects.select_related("role").get(username=username)
        except UsersTb.DoesNotExist:
            return Response({'error': 'Utilisateur non trouvé'}, status=status.HTTP_404_NOT_FOUND)

        if not check_password(password, user.user_pswd):
            return Response({'error': 'Mot de passe incorrect'}, status=status.HTTP_401_UNAUTHORIZED)

        # Génération correcte des tokens JWT à partir de l'utilisateur
        refresh = RefreshToken.for_user(user)
        # Ajouter des claims personnalisés dans le token d'actualisation si besoin
        refresh['role'] = user.role.role_name

        return Response({
            'refresh': str(refresh),
            'access': str(refresh.access_token),
            'user': {
                'user_id': user.user_id,
                'username': user.username,
                'role_id': user.role_id,
                'role_name': user.role.role_name
            }
        })
