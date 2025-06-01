from django.db.models import Q
from django.views.generic import ListView
from .models import Audio

class AudiosListView(ListView):
    """
    Lista los audios
    """
    model = Audio
    paginate_by = 8
    context_object_name = "audios"
    template_name = "audios/inicio.html"
    
    def get_queryset(self):
        """
        Filtra por genero y luego realiza busqueda desde el cuadro de texto
        """
        queryset = super().get_queryset()
        if genero := self.request.GET.get('g', ''):
            queryset = queryset.filter(genero__iexact=genero)
        if busqueda := self.request.GET.get('q', ''):
            queryset = queryset.filter(
                Q(titulo__icontains=busqueda) |
                Q(genero__icontains=busqueda)
            )
        self.conteo_resultados = queryset.count() 
        return queryset
    
    def get_context_data(self, **kwargs):
        """
        Agrega una lista de generos y devuelve los queryparams dentro del contexto
        """
        context = super().get_context_data(**kwargs)
        context.update({
            'q': self.request.GET.get('q', ''),
            'g': self.request.GET.get('g', ''),
            'conteo_resultados': self.conteo_resultados,
            'generos': Audio.objects.values_list('genero', flat=True).distinct()   # Pasamos la lista de géneros
        })
        return context
    