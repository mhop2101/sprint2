from django.db import models


class Paciente(models.Model):
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    fecha_nacimiento = models.DateField()
    direccion = models.TextField(blank=True, null=True)
    telefono = models.CharField(max_length=15, blank=True, null=True)
    email = models.EmailField(unique=True, blank=True, null=True)

    def __str__(self):
        return f"{self.nombre} {self.apellido}"

class Cita(models.Model):
    paciente = models.ForeignKey(Paciente, on_delete=models.CASCADE, related_name='citas')
    fecha = models.DateTimeField()
    hora_inicio = models.DateTimeField()
    hora_fin = models.DateTimeField()
    motivo = models.TextField(blank=True, null=True)
    notas = models.TextField(blank=True, null=True)

    def __str__(self):
        return f"Cita para {self.paciente} el {self.fecha}"
    
class ItemInventario(models.Model):
    nombre = models.CharField(max_length=255)

    def __str__(self):
        return self.nombre

class Insumo(models.Model):
    funcionalidad = models.CharField(max_length=255)
    ubicacion = models.CharField(max_length=255)
    id_item_inventario = models.ForeignKey(ItemInventario, on_delete=models.CASCADE)

    def __str__(self):
        return self.funcionalidad

class Dispositivo(models.Model):
    funcionalidad = models.CharField(max_length=255)
    posesion = models.CharField(max_length=255)
    id_item_inventario = models.ForeignKey(ItemInventario, on_delete=models.CASCADE)

    def __str__(self):
        return self.funcionalidad

class Medicamento(models.Model):
    uso = models.CharField(max_length=255)
    recomendaciones = models.CharField(max_length=255)
    dosis = models.CharField(max_length=255)
    id_item_inventario = models.ForeignKey(ItemInventario, on_delete=models.CASCADE)

    def __str__(self):
        return self.uso
