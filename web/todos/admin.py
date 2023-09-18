from django.contrib import admin

from .models import Todo


@admin.register(Todo)
class TodoAdmin(admin.ModelAdmin):
    date_hierarchy = "updated_at"
    list_display = ["id", "user", "title", "status", "created_at", "updated_at"]
    list_filter = ["status"]
    search_fields = ["user__username", "title"]
