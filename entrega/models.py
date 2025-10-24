from django.db import models
from recepcion.models import Paciente
from diagnostico.models import Estudiante

estado_choices = [("Pendiente", "Pendiente"),
                  ("Entregado", "Entregado"),
                  ("Devuelto", "Devuelto")]

# Create your models here.
class ReporteEntrega(models.Model):
    paciente = models.OneToOneField(Paciente, on_delete=models.CASCADE, related_name="reporte_entrega")
    diagnostico = models.ForeignKey(Estudiante, on_delete=models.SET_NULL, null=True, blank=True, related_name="reportes_entrega")
    estado = models.CharField(max_length=50,
                              choices=estado_choices,
                              default="Pendiente")
    observaciones = models.CharField(max_length=200)
    def __str__(self):
        return f"Entrega de: {self.paciente.cliente}"
