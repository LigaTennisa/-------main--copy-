from rest_framework import viewsets  # Django REST Framework позволяет объединить логику для набора связанных представлений в одном классе, называемом a ViewSet

from userss.serializers import UserSerializer
from .models import User


class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = User.objects.all()
    serializer_class = UserSerializer
    # permission_classes = [permissions.IsAuthenticated]
