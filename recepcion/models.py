from django.db import models

#EL paciente tiene un cliente su equipo y un problema que quiere solucionar
class Paciente(models.Model):
    cliente =  models.CharField(max_length=50)
    equipo =  models.CharField(max_length=50)
    problema =  models.CharField(max_length=50)
    def __str__(self):
        return f"{self.cliente} - {self.equipo}"

# Create your models here.
