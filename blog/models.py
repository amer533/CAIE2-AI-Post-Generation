from django.db import models


class User(models.Model):
    name = models.CharField(max_length=100)
    phone_number = models.CharField(max_length=20, unique=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.name


class post(models.Model):
    user = models.ForeignKey(
    User,
    on_delete=models.CASCADE,
    related_name="posts",
    null=True,
    blank=True
)

    title_id = models.BigAutoField(primary_key=True)
    titel = models.CharField(max_length=100)
    contant = models.TextField(max_length=200)
    date = models.DateField()


class Comment(models.Model):
    post = models.ForeignKey(
        post,
        on_delete=models.CASCADE,
        related_name="comments"
    )
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name="comments"
    )
    text = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Comment by {self.user.name}"