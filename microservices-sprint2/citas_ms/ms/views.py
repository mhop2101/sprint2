from django.shortcuts import render

from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .models import Paciente
from .models import Cita
import json
import requests


@csrf_exempt
def crear_cita(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        paciente_id = data.get('paciente_id')
        fecha = data.get('fecha')
        motivo = data.get('motivo', None)
        notas = data.get('notas', None)
        

        try:
            paciente = Paciente.objects.get(pk=paciente_id)
        except Paciente.DoesNotExist:
            return JsonResponse({'error': 'Paciente no encontrado'}, status=404)

        cita = Cita(
            paciente=paciente,
            fecha=fecha,
            motivo=motivo,
            notas=notas
        )
        cita.save()

        return JsonResponse({'message': 'Cita creada con éxito', 'id': cita.id}, status=201)

    return JsonResponse({'error': 'Método no permitido'}, status=405)


def obtener_todas_citas(request):
    if request.method == 'GET':
        citas = Cita.objects.all()
        citas_list = [{"id": cita.id, "fecha": cita.fecha, "motivo": cita.motivo,
                       "notas": cita.notas, "paciente": cita.paciente.id} for cita in citas]
        msg = f'Todas las citas'
        return render(request, 'citas.html', {'citas': citas_list, 'msg': msg})
        #return JsonResponse(citas_list, safe=False)

    return JsonResponse({'error': 'Método no permitido'}, status=405)


def obtener_citas_paciente(request, paciente_id):
    if request.method == 'GET':
        try:
            citas = Cita.objects.filter(paciente_id=paciente_id)
            citas_list = [{"id": cita.id, "fecha": cita.fecha,
                           "motivo": cita.motivo, "notas": cita.notas} for cita in citas]
            msg = f'Citas del Paciente: {paciente_id}'
            return render(request, 'citas.html', {'citas': citas_list, 'msg': msg})
            return JsonResponse(citas_list, safe=False)
        except Paciente.DoesNotExist:
            return JsonResponse({'error': 'Paciente no encontrado'}, status=404)

    return JsonResponse({'error': 'Método no permitido'}, status=405)
