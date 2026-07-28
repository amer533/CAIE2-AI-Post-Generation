from rest_framework import serializers
from blog.models.user import User


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = [
            "id",
            "name",
            "phone_number",
            "created_at",
            "updated_at",
            "is_active",
        ]