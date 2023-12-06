from django.urls import path
from . import views

urlpatterns = [
    path('crear_sede/', views.crear_sede, name='crear_sede'),
    path('listar_sedes/', views.listar_sedes, name='listar_sedes'),
]
