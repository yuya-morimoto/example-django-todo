from django.urls import path

from . import views

app_name = "todos"

urlpatterns = [
    path("", views.IndexView.as_view(), name="index"),
    path("<uuid:pk>/", views.TodoDetailView.as_view(), name="detail"),
    path("create/", views.TodoCreateView.as_view(), name="create"),
]
