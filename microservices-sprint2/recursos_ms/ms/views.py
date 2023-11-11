from django.shortcuts import render, get_object_or_404
from django.http import JsonResponse
import json
from .models import ItemInventario
from django.views.decorators.csrf import csrf_exempt


def darmensaje(request):
    return JsonResponse({'Servicio no disponible': 'error 500'}, status=200)

def health(request):
    return JsonResponse({'ok': 'ok'}, status=200)