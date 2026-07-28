from rest_framework.decorators import api_view
from rest_framework.response import Response

from blog.models.user import User
from blog.serializers import UserSerializer


@api_view(["GET"])
def get_active_users(request):
    users = User.objects.filter(is_active=True)

    serializer = UserSerializer(users, many=True)

    return Response(serializer.data)