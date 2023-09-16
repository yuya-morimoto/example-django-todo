from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth.views import LoginView as BaseSigninView
from django.contrib.auth.views import LogoutView as BaseSignoutView
from django.shortcuts import resolve_url
from django.urls import reverse_lazy
from django.views.generic import CreateView, TemplateView


class IndexView(TemplateView):
    template_name = "index.html"


class SignupView(CreateView):
    form_class = UserCreationForm
    template_name = "signup.html"
    success_url = reverse_lazy("accounts:index")


class SigninView(BaseSigninView):
    form_class = AuthenticationForm
    template_name = "signin.html"

    def get_default_redirect_url(self):  # type: ignore
        if self.next_page:
            return resolve_url(self.next_page)
        else:
            return reverse_lazy("accounts:index")


class SignoutView(BaseSignoutView):
    success_url = reverse_lazy("accounts:index")

    def get_default_redirect_url(self):  # type: ignore
        if self.next_page:
            return resolve_url(self.next_page)
        else:
            return reverse_lazy("accounts:index")
