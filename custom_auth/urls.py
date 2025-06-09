from django.urls import path
from django.contrib.auth.views import LogoutView
from . import views

app_name = "custom_auth"

urlpatterns = [
    path('login', views.LoginView.as_view(), name="login"),
    path('logout', LogoutView.as_view(), name="logout"), # https://docs.djangoproject.com/en/5.2/topics/auth/default/#using-the-views
    path('register', views.RegisterView.as_view(), name="register"),
    path('dashboard', views.DashboardView.as_view(), name="dashboard"),
] 