from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

from ai.content.content_service import (
    ContentServiceError,
    generate_post,
)


@api_view(["POST"])
def generate_post_view(request):
    title = request.data.get("title")
    tone = request.data.get("tone")

    try:
        result = generate_post(title, tone)

        return Response(
            result,
            status=status.HTTP_200_OK,
        )

    except ValueError as error:
        return Response(
            {"error": str(error)},
            status=status.HTTP_400_BAD_REQUEST,
        )

    except ContentServiceError as error:
        return Response(
            {"error": str(error)},
            status=status.HTTP_503_SERVICE_UNAVAILABLE,
        )