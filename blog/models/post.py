from django.db import models
from .user import User


class post(models.Model):
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name="posts",
        null=True,
        blank=True,
    )

    title_id = models.BigAutoField(primary_key=True)
    titel = models.CharField(max_length=100)
    contant = models.TextField(max_length=200)
    date = models.DateField()

    summary = models.TextField(
        blank=True,
        default="",
    )

    summary_generated_at = models.DateTimeField(
        blank=True,
        null=True,
    )