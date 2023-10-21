from django.urls import path
from . import views

urlpatterns = [
    path('crear_recurso/', views.crear_recurso, name='crear_recurso'),
    path('buscar_recurso/<int:recurso_id>/', views.buscar_recurso, name='buscar_recurso'),
    path('recursos/', views.recursos, name='recursos'),
    
]
