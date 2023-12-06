from django.urls import path
from . import views

urlpatterns = [
    path('crear_recurso/', views.crear_inventario, name='crear_inventario'),
    path('listar_recursos/', views.listar_recursos, name='listar_recursos'),
]