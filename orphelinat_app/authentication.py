from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.contrib.auth.hashers import check_password
from rest_framework_simplejwt.tokens import RefreshToken
from orphelinat_app.models import UsersTb
from orphelinat_app.serializers import UsersTbSerializer


class LoginUserView(APIView):
    def post(self, request):
        username = request.data.get("username")
        password = request.data.get("password")

        if not username or not password:
            return Response({"error": "Nom d'utilisateur et mot de passe requis."}, status=status.HTTP_400_BAD_REQUEST)

        try:
            user = UsersTb.objects.get(username=username)
        except UsersTb.DoesNotExist:
            return Response({"error": "Utilisateur non trouvé."}, status=status.HTTP_404_NOT_FOUND)

        if not check_password(password, user.user_pswd):
            return Response({"error": "Mot de passe incorrect."}, status=status.HTTP_401_UNAUTHORIZED)

        refresh = RefreshToken.for_user(user)
        serializer = UsersTbSerializer(user)

        return Response({
            "refresh": str(refresh),
            "access": str(refresh.access_token),
            "user": serializer.data,
        }, status=status.HTTP_200_OK)
