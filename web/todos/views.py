from typing import Any
from uuid import UUID

from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import AnonymousUser
from django.http import HttpResponse
from django.shortcuts import get_object_or_404
from django.urls import reverse_lazy
from django.views.generic import CreateView as BaseCreateView
from django.views.generic import TemplateView

from .forms import TodoForm
from .models import Todo


class IndexView(LoginRequiredMixin, TemplateView):
    template_name = "todos/index.html"

    def get_context_data(self, **kwargs: Any) -> dict[str, Any]:
        context = super().get_context_data(**kwargs)
        user = self.request.user
        if isinstance(user, AnonymousUser):
            context["todos"] = []
        else:
            context["todos"] = Todo.objects.filter(user=user)
        return context


class DetailView(LoginRequiredMixin, TemplateView):
    template_name = "todos/detail.html"

    def get_context_data(self, **kwargs: Any) -> dict[str, Any]:
        context = super().get_context_data(**kwargs)
        user = self.request.user
        todo_id: UUID = self.kwargs.get("todo_id")
        if isinstance(user, AnonymousUser):
            context["todo"] = []
        else:
            todo: Todo = get_object_or_404(Todo, pk=todo_id, user=user)
            context["todo"] = todo
        return context


class CreateView(LoginRequiredMixin, BaseCreateView):
    form_class = TodoForm
    template_name = "todos/create.html"
    success_url = reverse_lazy("todos:index")

    def form_valid(self, form: TodoForm) -> HttpResponse:
        form.instance.user = self.request.user
        return super().form_valid(form)
