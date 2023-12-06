from django.http import JsonResponse, HttpResponse
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_http_methods
from django.shortcuts import render
import json
from .models import Sede

@csrf_exempt
@require_http_methods(["POST"])
def crear_sede(request):
    try:
        data = json.loads(request.body)
        nombre = data.get('nombre')
        direccion = data.get('direccion')
        caracteristicas = data.get('caracteristicas')

        sede = Sede(nombre=nombre, direccion=direccion, caracteristicas=caracteristicas)
        sede.save()

        return JsonResponse({'mensaje': 'Sede creada con éxito'}, status=201)

    except json.JSONDecodeError:
        return JsonResponse({'error': 'Formato de solicitud inválido'}, status=400)
    except Exception as e:
        return JsonResponse({'error': str(e)}, status=500)


def listar_sedes(request):
    sedes = Sede.objects.all()
    return render(request, 'listar_sedes.html', {'sedes': sedes})
