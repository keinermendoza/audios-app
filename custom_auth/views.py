from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.contrib.auth import get_user_model, login
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import LoginView as BaseLoginView

from django.views.generic import CreateView, UpdateView, TemplateView
from .forms import LoginCustomUser, RegisterCustomUser, EditCustomUserForm

User = get_user_model()

class LoginView(BaseLoginView):
    template_name="auth/login.html"
    redirect_authenticated_user=True
    authentication_form=LoginCustomUser

class RegisterView(CreateView):
    model = User 
    form_class = RegisterCustomUser
    template_name ="auth/register.html"

    def form_valid(self, form):
        """
        Agregado temporalmente hasta implementar la validacion por email con SMTP
        """
        user = form.save()
        login(self.request, user)
        return redirect('custom_auth:dashboard')

class DashboardView(LoginRequiredMixin, TemplateView):
    template_name = "auth/dashboard.html"

class EditProfile(LoginRequiredMixin, UpdateView):
    model = User
    form_class = EditCustomUserForm
    success_url = reverse_lazy('custom_auth:dashboard')
    template_name ="auth/profile_edit.html"

    def get_object(self):
        return self.request.user

    