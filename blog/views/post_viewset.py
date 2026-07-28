from rest_framework import viewsets

from blog.models.post import post
from blog.serializers import PostSerializer


class PostViewSet(viewsets.ModelViewSet):
    queryset = post.objects.all()
    serializer_class = PostSerializer