from django.urls import path
from . import views

urlpatterns = [
    path('crear_cita/', views.crear_cita, name='crear_cita'),
    path('obtener_todas_citas/', views.obtener_todas_citas,
         name='obtener_todas_citas'),
    path('obtener_citas_paciente/<int:paciente_id>/',
         views.obtener_citas_paciente, name='obtener_citas_paciente'),
    path('health/',
         views.health, name='health'),
]
