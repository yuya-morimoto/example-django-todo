import uuid

from django.db import models


class Todo(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    title = models.CharField(
        max_length=100,
    )

    class Meta:
        verbose_name = "todo"
        verbose_name_plural = "todos"
