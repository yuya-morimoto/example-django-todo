import uuid

from django.conf import settings
from django.db import models


class StatusChoices(models.TextChoices):
    TODO = "01", "Todo"
    DOING = "02", "Doing"
    DONE = "03", "Done"


class Todo(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="user_todos"
    )
    title = models.CharField(
        max_length=100,
    )
    description = models.TextField(max_length=400, null=True, blank=True)
    status = models.CharField(
        max_length=2,
        choices=StatusChoices.choices,
        default=StatusChoices.TODO,
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "todo"
        verbose_name_plural = "todos"
