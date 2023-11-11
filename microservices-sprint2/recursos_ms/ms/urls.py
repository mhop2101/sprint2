from django.urls import path
from . import views

urlpatterns = [
    path('obtener_todas_citas/', views.darmensaje, name='darmensaje'),
    path('health/', views.health, name='health'),
]
