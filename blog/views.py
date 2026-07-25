from django.shortcuts import render

from blog.models import User
from django.http import HttpResponse

from rest_framework import serializers, status, viewsets
from rest_framework.decorators import api_view
from rest_framework.response import Response

from .models import post as Post

from .serializers import UserSerializer

from ai.content.content_service import generate_post

# Create your views here.


class PostSerializer(serializers.ModelSerializer):
    class Meta: 
        model = Post
        fields = "__all__"

class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer


@api_view(["GET"])
def get_active_users(request):
    users = User.objects.filter(is_active=True)

    serializer = UserSerializer(users, many=True)

    return Response(serializer.data)

@api_view(["POST"])
def generate_post_view(request):
    title = request.data.get("title")
    tone = request.data.get("tone")

    try:
        result = generate_post(title, tone)
        return Response(result, status=status.HTTP_200_OK)

    except ValueError as error:
        return Response(
            {"error": str(error)},
            status=status.HTTP_400_BAD_REQUEST,
        )

