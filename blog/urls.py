from django.urls import path

from .views import get_active_users, generate_post_view
from blog.views import summarize_post_view

urlpatterns = [
    path("users/active/", get_active_users, name="active-users"),
    path("posts/generate/", generate_post_view, name="generate-post"),
    path("posts/summarize/<int:post_id>/", summarize_post_view, name="summarize-post"),
]