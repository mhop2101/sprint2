from django.shortcuts import render
from .models import Paciente
from .models import Cita
from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import render, get_object_or_404
from django.http import JsonResponse, HttpResponse
import json


# Create your views here.

@csrf_exempt
def crear_paciente(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        nombre = data.get('nombre')
        apellido = data.get('apellido')
        fecha_nacimiento = data.get('fecha_nacimiento')
        direccion = data.get('direccion', None)
        telefono = data.get('telefono', None)
        email = data.get('email', None)
        
        integrity_user= data.get('integrity')
        integrity = abs(hash(nombre + apellido + "my_secret_password"))
        
        if integrity != integrity_user:
            return JsonResponse({'error': 'Integridad de datos comprometida hacker detectado !!!aAAAAA'}, status=400)
        
        paciente = Paciente(
            nombre=nombre,
            apellido=apellido,
            fecha_nacimiento=fecha_nacimiento,
            direccion=direccion,
            telefono=telefono,
            email=email
        )
        paciente.save()

        return JsonResponse({'message': 'Paciente creado con éxito', 'id': paciente.id}, status=201)

    return JsonResponse({'error': 'Método no permitido'}, status=405)


def buscar_paciente(request, paciente_id):
    # Obtiene el paciente por su id o devuelve un error 404 si no se encuentra.
    try:
        paciente = Paciente.objects.get(pk=paciente_id)

        # Renderiza un template (por ejemplo, 'paciente_detalle.html') y le pasa el paciente como contexto.
        return render(request, 'pacientes.html', {'pacientes': [paciente], 'msg':'Datos del paciente con id: '+str(paciente_id)})
    except:
        return HttpResponse("Paciente no encontrado", status=404)
    


def pacientes(request):
    # Obtiene todos los pacientes.
    todos_pacientes = Paciente.objects.all()

    # Renderiza un template (por ejemplo, 'pacientes_lista.html') y le pasa los pacientes como contexto.
    return render(request, 'pacientes.html', {'pacientes': todos_pacientes, 'msg':'Todos los pacientes'})


def health(request):
    return JsonResponse({'ok': 'ok'}, status=200)