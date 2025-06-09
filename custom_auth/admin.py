from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser

@admin.register(CustomUser)
class CustomUserAdmin(UserAdmin):
    list_display = ["email", "username", "get_full_name", "is_admin", "is_active", "ultimo_login", "fecha_registro"]
    list_display_links = ["email", "get_full_name"]
    ordering = ["-fecha_registro"]
    readonly_fields = ["ultimo_login", "fecha_registro"]
    filter_horizontal = []
    list_filter = []
    fieldsets = []

    @admin.display(ordering='nombre', description='Nombre completo')
    def get_full_name(self, obj):
        return f"{obj.nombre} {obj.apellido}"
