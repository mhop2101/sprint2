from django.http import JsonResponse, HttpResponse
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_http_methods
import json
from .models import Insumo, Dispositivo, Medicamento, ItemInventario
from django.shortcuts import render
from .models import Insumo, Dispositivo, Medicamento

@csrf_exempt
@require_http_methods(["POST"])
def crear_inventario(request):
    try:
        data = json.loads(request.body)
        tipo = data.get('tipo')

        # Crear un nuevo ItemInventario
        item_inventario = ItemInventario(nombre=data.get('nombre_item_inventario'))
        item_inventario.save()

        if tipo == 'insumo':
            # Crear un nuevo Insumo
            insumo = Insumo(
                funcionalidad=data.get('funcionalidad'),
                ubicacion=data.get('ubicacion'),
                id_item_inventario=item_inventario
            )
            insumo.save()
            return JsonResponse({'mensaje': 'Insumo creado con éxito'}, status=201)

        elif tipo == 'dispositivo':
            # Crear un nuevo Dispositivo
            dispositivo = Dispositivo(
                funcionalidad=data.get('funcionalidad'),
                posesion=data.get('posesion'),
                id_item_inventario=item_inventario
            )
            dispositivo.save()
            return JsonResponse({'mensaje': 'Dispositivo creado con éxito'}, status=201)

        elif tipo == 'medicamento':
            # Crear un nuevo Medicamento
            medicamento = Medicamento(
                uso=data.get('uso'),
                recomendaciones=data.get('recomendaciones'),
                dosis=data.get('dosis'),
                id_item_inventario=item_inventario
            )
            medicamento.save()
            return JsonResponse({'mensaje': 'Medicamento creado con éxito'}, status=201)

        else:
            return JsonResponse({'error': 'Tipo no válido'}, status=400)

    except json.JSONDecodeError:
        return JsonResponse({'error': 'Formato de solicitud inválido'}, status=400)
    except Exception as e:
        return JsonResponse({'error': str(e)}, status=500)
    

def listar_recursos(request):
    insumos = Insumo.objects.all()
    dispositivos = Dispositivo.objects.all()
    medicamentos = Medicamento.objects.all()

    return render(request, 'listar_recursos.html', {
        'insumos': insumos,
        'dispositivos': dispositivos,
        'medicamentos': medicamentos
    })
