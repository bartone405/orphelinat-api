# orphelinat_app/swagger.py

from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

schema_view = get_schema_view(
    openapi.Info(
        title="API Orphelinat",
        default_version='v1',
        description="Documentation API Orphelinat",
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),  # Accès public au swagger
)
