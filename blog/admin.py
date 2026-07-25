from django.contrib import admin
from .models import User, post, Comment


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = (
        "name",
        "phone_number",
        "is_active",
        "created_at",
        "updated_at",
    )
    search_fields = ("name", "phone_number")
    list_filter = ("is_active",)


@admin.register(post)
class PostAdmin(admin.ModelAdmin):
    list_display = ("title_id", "titel", "user", "date")
    search_fields = ("titel", "contant", "user__name")
    list_filter = ("date",)


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ("post", "user", "created_at")
    search_fields = ("text", "user__name")
    list_filter = ("created_at",)