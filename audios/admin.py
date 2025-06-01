from django.contrib import admin
from import_export.admin import ImportExportMixin
from .models import Audio
from .resources import AudioResource

@admin.register(Audio)
class AudioAdmin(ImportExportMixin, admin.ModelAdmin):
    resource_class = AudioResource
    list_display = ('titulo', 'genero', 'compositor', 'interprete')  # Campos visibles en la lista
    search_fields = ('titulo', 'genero', 'compositor', 'interprete')  # Campos que se pueden buscar

