from django.shortcuts import render
from .models import Horario


def index(request):
    return render(request, 'index.html')


from django.db.models import Count
from django.shortcuts import render
from .models import Horario

def horarios_views(request):
    origen_filtrado = request.GET.get('origen')
    origenes_disponibles = Horario.objects.values_list('origen', flat=True).distinct()

    if origen_filtrado:
        horarios = Horario.objects.filter(origen=origen_filtrado)
    else:
        horarios = Horario.objects.all()
    rutas = {}
    for h in horarios:
        key = (h.origen, h.destino)
        if key not in rutas:
            rutas[key] = []
        rutas[key].append(h)
    rutas_lista = [
        {
            'origen': origen,
            'destino': destino,
            'horarios': datos
        }
        for (origen, destino), datos in rutas.items()
    ]
    rutas_lista.sort(key=lambda r: (0 if r['origen'].lower().startswith('valdivia') else 1, r['origen'], r['destino']))

    return render(request, 'horarios.html', {
        'rutas': rutas_lista,
        'origenes': origenes_disponibles,
        'origen_filtrado': origen_filtrado
    })




def contacto(request):
    return render(request, 'contacto.html')

