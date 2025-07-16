from rest_framework.permissions import BasePermission

class IsAdminRole(BasePermission):
    """
    Autorise uniquement les utilisateurs avec le rôle 'admin',
    récupéré depuis le token JWT.
    """

    def has_permission(self, request, view):
        token = request.auth  # token JWT décodé

        if not token:
            return False

        role = token.get('role', '').lower() if isinstance(token, dict) else ''

        return role == 'admin'
