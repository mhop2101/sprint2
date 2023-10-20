from django.urls import path
from . import views

urlpatterns = [
    path('crear_paciente/', views.crear_paciente, name='crear_paciente'),
    path('buscar_paciente/<int:paciente_id>/', views.buscar_paciente, name='buscar_paciente'),
    path('pacientes/', views.pacientes, name='pacientes'),
    
]
