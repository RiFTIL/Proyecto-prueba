from django.contrib import admin
from .models import Horario
# Register your models here.

# Creamos una clase para personalizar la vista del admin
class HorarioAdmin(admin.ModelAdmin):
    # Columnas que se mostrarán en la lista de horarios
    list_display = ('origen', 'destino', 'dias', 'tarifa_adulto')

    # Filtros que aparecerán en una barra lateral
    list_filter = ('origen', 'destino')

    # Un campo de búsqueda que buscará por estos campos
    search_fields = ('origen', 'destino', 'dias')

admin.site.register(Horario, HorarioAdmin)