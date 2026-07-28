from django.shortcuts import get_object_or_404
from django.utils import timezone

from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

from ai.content.content_service import (
    ContentServiceError,
    summarize_post,
)
from blog.models.post import post


@api_view(["POST"])
def summarize_post_view(request, post_id):
    post_instance = get_object_or_404(
        post,
        pk=post_id,
    )

    try:
        generated_summary = summarize_post(
            post_instance.contant
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

    post_instance.summary = generated_summary
    post_instance.summary_generated_at = timezone.now()

    post_instance.save(
        update_fields=[
            "summary",
            "summary_generated_at",
        ]
    )

    return Response(
        {
            "post_id": post_instance.pk,
            "summary": post_instance.summary,
            "summary_generated_at": (
                post_instance.summary_generated_at
            ),
        },
        status=status.HTTP_200_OK,
    )