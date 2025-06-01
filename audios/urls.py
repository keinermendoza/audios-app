from django.contrib import admin
from django.urls import path
from .import views

urlpatterns = [
    path("", views.AudiosListView.as_view(), name='inicio')
]