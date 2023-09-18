from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import AnonymousUser
from django.db.models import QuerySet
from django.http import HttpResponse
from django.urls import reverse_lazy
from django.views.generic import CreateView, DeleteView, DetailView, ListView, UpdateView

from .forms import TodoForm
from .models import Todo


class IndexView(LoginRequiredMixin, ListView):
    template_name = "todos/index.html"
    context_object_name = "todo_list"
    model = Todo

    def get_queryset(self) -> QuerySet[Todo]:
        user = self.request.user
        if isinstance(user, AnonymousUser):
            return Todo.objects.none()
        else:
            return Todo.objects.filter(user=user)


class TodoDetailView(LoginRequiredMixin, DetailView):
    template_name = "todos/detail.html"
    context_object_name = "todo"
    model = Todo


class TodoCreateView(LoginRequiredMixin, CreateView):
    form_class = TodoForm
    template_name = "todos/create.html"
    success_url = reverse_lazy("todos:index")

    def form_valid(self, form: TodoForm) -> HttpResponse:
        form.instance.user = self.request.user
        return super().form_valid(form)


class TodoUpdateView(LoginRequiredMixin, UpdateView):
    form_class = TodoForm
    model = Todo
    template_name = "todos/update.html"
    success_url = reverse_lazy("todos:index")


class TodoDeleteView(LoginRequiredMixin, DeleteView):  # type: ignore [misc]
    template_name = "todos/delete.html"
    context_object_name = "todo"
    success_url = reverse_lazy("todos:index")
    model = Todo
