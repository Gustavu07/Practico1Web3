from django.db import models

from .cliente import Cliente
from .mesero import Mesero
from .mesa import Mesa
from .platos import Plato

class Orden(models.Model):
    ESTADO_CHOICES = [
        ('abierto', 'Abierto'),
        ('cerrado', 'Cerrado')
    ]

    fecha_hora = models.DateTimeField(auto_now_add=True)
    estado = models.CharField(max_length=10, choices=ESTADO_CHOICES, default='abierto')
    cliente = models.ForeignKey(Cliente, on_delete=models.SET_NULL, null=True, blank=True)
    mesero = models.ForeignKey(Mesero, on_delete=models.CASCADE)
    mesa = models.ForeignKey(Mesa, on_delete=models.CASCADE)

    platos = models.ManyToManyField(Plato)

    def __str__(self):
        return f"Orden {self.id} - {self.estado} - Mesa {self.mesa.numero}"
