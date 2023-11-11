from django.urls import path
from . import views

urlpatterns = [
    path('darmensaje/', views.darmensaje, name='darmensaje'),
]
