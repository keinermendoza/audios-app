from import_export import resources
from .models import Audio

class AudioResource(resources.ModelResource):
    class Meta:
        model = Audio
        import_id_fields = ('titulo',)
        fields = ('titulo', 'interprete', 'compositor', 'genero', 'derechos_autor', 'imagen', 'archivo')
