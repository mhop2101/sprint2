from django.shortcuts import render

from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .models import Paciente
from .models import Cita
import json
import requests
import hashlib
from datetime import datetime


@csrf_exempt
def crear_cita(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
        except json.JSONDecodeError:
            return JsonResponse({'error': 'Formato de datos inválido'}, status=400)

        paciente_id = data.get('paciente_id')
        fecha = data.get('fecha')
        hora_inicio = data.get('hora_inicio')
        hora_fin = data.get('hora_fin')
        motivo = data.get('motivo', None)
        notas = data.get('notas', None)
        
        integrity_user= data.get('integrity')
        integrity = hashlib.md5(f"{motivo} + {notas} + {paciente_id} + my_secret_password".encode('utf-8')).hexdigest()
        
        print("integrity_user",integrity_user)
        print("integrity",integrity)
        print(motivo + "my_secret_password")
        
        if str(integrity) != str(integrity_user):
            return JsonResponse({'error': 'Integridad de datos comprometida hacker detectado !!!aAAAAA'}, status=400)

        if not all([paciente_id, fecha, hora_inicio, hora_fin]):
            return JsonResponse({'error': 'Datos faltantes'}, status=400)

        try:
            paciente = Paciente.objects.get(pk=paciente_id)
        except Paciente.DoesNotExist:
            return JsonResponse({'error': 'Paciente no encontrado'}, status=404)

        cita = Cita(
            paciente=paciente,
            fecha=fecha,
            hora_inicio=hora_inicio,
            hora_fin=hora_fin,
            motivo=motivo,
            notas=notas
        )
        cita.save()

        return JsonResponse({'message': 'Cita creada con éxito', 'id': cita.id}, status=201)

    return JsonResponse({'error': 'Método no permitido'}, status=405)

def crear_cita_2(request):
    if request.method == 'POST':
        
        paciente_id = request.POST.get('paciente_id')
        fecha_str = request.POST.get('fecha')
        hora_inicio_str = request.POST.get('hora_inicio')
        hora_fin_str = request.POST.get('hora_fin')

        formato_fecha = '%Y-%m-%d'
        formato_hora = '%H:%M'

        fecha = datetime.strptime(fecha_str, formato_fecha)
        hora_inicio = datetime.strptime(hora_inicio_str, formato_hora)
        hora_fin = datetime.strptime(hora_fin_str, formato_hora)

        # Combinar fecha con hora
        fecha_hora_inicio = fecha.replace(hour=hora_inicio.hour, minute=hora_inicio.minute)
        fecha_hora_fin = fecha.replace(hour=hora_fin.hour, minute=hora_fin.minute)
        motivo = request.POST.get('motivo', None)
        notas = request.POST.get('notas', None)

        # Logica para verificar la integridad de los datos
        # ...

        if not all([paciente_id, fecha, hora_inicio, hora_fin]):
            return JsonResponse({'error': 'Datos faltantes'}, status=400)

        try:
            paciente = Paciente.objects.get(pk=paciente_id)
        except Paciente.DoesNotExist:
            return JsonResponse({'error': 'Paciente no encontrado'}, status=404)

        cita = Cita(
            paciente=paciente,
            fecha=fecha,
            hora_inicio=hora_inicio,
            hora_fin=hora_fin,
            motivo=motivo,
            notas=notas
        )
        cita.save()

        return JsonResponse({'message': 'Cita creada con éxito', 'id': cita.id}, status=201)

    elif request.method == 'GET':
        return render(request, 'crear_cita.html')

    else:
        return JsonResponse({'error': 'Método no permitido'}, status=405)


def obtener_todas_citas(request):
    if request.method == 'GET':
        citas = Cita.objects.all()
        citas_list = [{
            "id": cita.id,
            "fecha": cita.fecha.strftime('%Y-%m-%d %H:%M'),
            "hora_inicio": cita.hora_inicio.strftime('%H:%M'),
            "hora_fin": cita.hora_fin.strftime('%H:%M'),
            "motivo": cita.motivo,
            "notas": cita.notas,
            "paciente_id": cita.paciente.id,
            "paciente_nombre": f"{cita.paciente.nombre} {cita.paciente.apellido}"
        } for cita in citas]

        msg = 'Todas las citas'
        
        # Descomenta la siguiente línea si deseas retornar una respuesta JSON
        # return JsonResponse(citas_list, safe=False)

        # Renderiza la plantilla HTML con las citas
        return render(request, 'citas.html', {'citas': citas_list, 'msg': msg})

    return JsonResponse({'error': 'Método no permitido'}, status=405)


def obtener_citas_paciente(request, paciente_id):
    if request.method == 'GET':
        if not Paciente.objects.filter(pk=paciente_id).exists():
            return JsonResponse({'error': 'Paciente no encontrado'}, status=404)

        citas = Cita.objects.filter(paciente=paciente_id)
        citas_list = [{
            "id": cita.id,
            "fecha": cita.fecha.strftime('%Y-%m-%d %H:%M'),
            "hora_inicio": cita.hora_inicio.strftime('%H:%M'),
            "hora_fin": cita.hora_fin.strftime('%H:%M'),
            "motivo": cita.motivo,
            "notas": cita.notas
        } for cita in citas]

        msg = f'Citas del Paciente: {paciente_id}'
        
        # Descomenta la siguiente línea si deseas retornar una respuesta JSON
        # return JsonResponse(citas_list, safe=False)

        # Renderiza la plantilla HTML con las citas
        return render(request, 'citas.html', {'citas': citas_list, 'msg': msg})

    return JsonResponse({'error': 'Método no permitido'}, status=405)

def health(request):
    return JsonResponse({'ok': 'ok'}, status=200)
