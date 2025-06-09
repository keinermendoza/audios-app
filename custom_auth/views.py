from django.urls import reverse_lazy
from django.contrib.auth import get_user_model
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import LoginView as BaseLoginView
from django.views.generic import CreateView, TemplateView
from .forms import LoginCustomUser, RegisterCustomUser

class LoginView(BaseLoginView):
    template_name="auth/login.html"
    redirect_authenticated_user=True
    authentication_form=LoginCustomUser

class RegisterView(CreateView):
    template_name ="auth/register.html"
    success_url = reverse_lazy("custom_auth:login")
    form_class = RegisterCustomUser
    model = get_user_model()

class DashboardView(LoginRequiredMixin, TemplateView):
    template_name = "auth/dashboard.html"