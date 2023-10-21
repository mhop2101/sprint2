from django.shortcuts import render, get_object_or_404
from django.http import JsonResponse
import json
from .models import Recurso
from django.views.decorators.csrf import csrf_exempt


@csrf_exempt
def crear_recurso(request):
    if request.method == "POST":
        data = json.loads(request.body.decode('utf-8'))
        nombre = data.get('nombre')
        cantidad = data.get('cantidad')

        if nombre and cantidad is not None:
            recurso = Recurso(nombre=nombre, cantidad=cantidad)
            recurso.save()
            return JsonResponse({"message": "Recurso creado con éxito", "id": recurso.id}, status=201)
        else:
            return JsonResponse({"error": "Datos inválidos"}, status=400)

    return JsonResponse({"error": "Método no permitido"}, status=405)

def buscar_recurso(request, recurso_id):
    recurso = get_object_or_404(Recurso, id=recurso_id)
    return render(request, 'detalle_recurso.html', {'recurso': recurso})

def recursos(request):
    lista_recursos = Recurso.objects.all()
    return render(request, 'lista_recursos.html', {'recursos': lista_recursos})
