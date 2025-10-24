from django.db import models
from recepcion.models import Paciente
# Create your models here.
TIPO_DIAGNOSTICO_CHOICES = [
    ("Preventivo","Preventivo"),
    ("correctivo","Correctivo"),
]
class Estudiante(models.Model):
        estudiante=models.CharField(max_length=50)
        equipo = models.ForeignKey(Paciente,on_delete=models.CASCADE,related_name="Equipo_diagnosticado")
        diagnostico=models.CharField(max_length=50)
        solucion=models.CharField(max_length=50)
        tipo = models.CharField(
        max_length=20, 
        choices=TIPO_DIAGNOSTICO_CHOICES,
        default="Preventivo"
        )
        def __str__(self):
            return f"Evaluacion de {self.estudiante} hacia {self.equipo}"
