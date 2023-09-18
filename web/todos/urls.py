from django.urls import path

from . import views

app_name = "todos"

urlpatterns = [
    path("", views.IndexView.as_view(), name="index"),
    path("<uuid:todo_id>/", views.DetailView.as_view(), name="detail"),
    path("create/", views.CreateView.as_view(), name="create"),
]
