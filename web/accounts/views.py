from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth.views import LoginView as BaseSigninView
from django.contrib.auth.views import LogoutView as BaseSignoutView
from django.urls import reverse_lazy
from django.views.generic import CreateView, TemplateView


class IndexView(TemplateView):
    template_name = "accounts/index.html"


class SignupView(CreateView):
    form_class = UserCreationForm
    template_name = "accounts/signup.html"
    success_url = reverse_lazy("accounts:index")


class SigninView(BaseSigninView):
    form_class = AuthenticationForm
    template_name = "accounts/signin.html"


class SignoutView(BaseSignoutView):
    success_url = reverse_lazy("accounts:index")
