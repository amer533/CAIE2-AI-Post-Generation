from datetime import date
from unittest.mock import patch

from django.test import TestCase
from django.urls import reverse

from ai.content.content_service import ContentServiceError
from blog.models.post import post


class SummarizePostViewTests(TestCase):
    def setUp(self):
        self.post = post.objects.create(
            titel="Django Architecture",
            contant=(
                "Django applications benefit from separating HTTP handling, "
                "business logic, and external AI provider communication."
            ),
            date=date.today(),
        )

    @patch("blog.views.summarize.summarize_post")
    def test_summarize_post_saves_result(self, mock_summarize):
        mock_summarize.return_value = (
            "Django benefits from separating system responsibilities."
        )

        url = reverse(
            "summarize-post",
            kwargs={"post_id": self.post.pk},
        )

        response = self.client.post(url)

        self.assertEqual(response.status_code, 200)

        self.post.refresh_from_db()

        self.assertEqual(
            self.post.summary,
            "Django benefits from separating system responsibilities.",
        )

        self.assertIsNotNone(
            self.post.summary_generated_at
        )

        mock_summarize.assert_called_once_with(
            self.post.contant
        )

    def test_summarize_post_returns_404_when_post_not_found(self):
        url = reverse(
            "summarize-post",
            kwargs={"post_id": 999999},
        )

        response = self.client.post(url)

        self.assertEqual(response.status_code, 404)

    @patch("blog.views.summarize.summarize_post")
    def test_summarize_post_returns_503_when_ai_service_fails(
        self,
        mock_summarize,
    ):
        mock_summarize.side_effect = ContentServiceError(
            "AI content service is unavailable."
        )

        url = reverse(
            "summarize-post",
            kwargs={"post_id": self.post.pk},
        )

        response = self.client.post(url)

        self.assertEqual(response.status_code, 503)

        self.assertEqual(
            response.data["error"],
            "AI content service is unavailable.",
        )

    @patch("blog.views.summarize.summarize_post")
    def test_summarize_post_returns_400_for_invalid_content(
        self,
        mock_summarize,
    ):
        mock_summarize.side_effect = ValueError(
            "Post content is too short."
        )

        url = reverse(
            "summarize-post",
            kwargs={"post_id": self.post.pk},
        )

        response = self.client.post(url)

        self.assertEqual(response.status_code, 400)

        self.assertEqual(
            response.data["error"],
            "Post content is too short.",
        )