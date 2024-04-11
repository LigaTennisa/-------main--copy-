from rest_framework import viewsets  # Django REST Framework позволяет объединить логику для набора связанных представлений в одном классе, называемом a ViewSet

from postss.serializers import PostSerializer
from .models import Post


class PostViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    # permission_classes = [permissions.IsAuthenticated]