from rest_framework import generics, status
from rest_framework.response import Response
from django.contrib.auth.hashers import make_password
from orphelinat_app.models import UsersTb
from orphelinat_app.serializers import UsersTbSerializer


class RegisterUserView(generics.CreateAPIView):
    queryset = UsersTb.objects.all()
    serializer_class = UsersTbSerializer

    def create(self, request, *args, **kwargs):
        data = request.data.copy()

        # Hash le mot de passe avant de sauvegarder
        if 'user_pswd' in data:
            data['user_pswd'] = make_password(data['user_pswd'])

        serializer = self.get_serializer(data=data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)

        return Response(serializer.data, status=status.HTTP_201_CREATED)
