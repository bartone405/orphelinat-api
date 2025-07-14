from rest_framework import generics, status
from rest_framework.response import Response
from django.contrib.auth.hashers import make_password
from .models import UsersTb
from .serializers import UsersTbSerializer

class RegisterUserView(generics.CreateAPIView):
    queryset = UsersTb.objects.all()
    serializer_class = UsersTbSerializer

    def post(self, request, *args, **kwargs):
        data = request.data.copy()
        # Hacher le mot de passe
        if 'user_pswd' in data:
            data['user_pswd'] = make_password(data['user_pswd'])

        serializer = self.get_serializer(data=data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
