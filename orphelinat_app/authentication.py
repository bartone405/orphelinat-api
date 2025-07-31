from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework import status
from django.contrib.auth.models import User
from .models import UsersTb
from .serializers import LoginSerializer  # Import du serializer

class LoginUserView(APIView):
    def post(self, request):
        # Validation des données reçues avec LoginSerializer
        serializer = LoginSerializer(data=request.data)
        if not serializer.is_valid():
            return Response({'error': 'Veuillez fournir username et password'}, status=status.HTTP_400_BAD_REQUEST)

        username = serializer.validated_data.get("username")
        password = serializer.validated_data.get("password")

        try:
            user_obj = UsersTb.objects.get(username=username)
        except UsersTb.DoesNotExist:
            return Response({'error': 'Utilisateur non trouvé'}, status=status.HTTP_404_NOT_FOUND)

        # Comparaison simple du mot de passe en clair
        if password == user_obj.user_pswd:
            # Création d’un utilisateur Django factice pour JWT
            user = User(username=user_obj.username)
            user.id = user_obj.user_id
            user.is_active = True

            refresh = RefreshToken.for_user(user)
            return Response({
                'refresh': str(refresh),
                'access': str(refresh.access_token),
            }, status=status.HTTP_200_OK)

        return Response({'error': 'Mot de passe incorrect'}, status=status.HTTP_401_UNAUTHORIZED)
