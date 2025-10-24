from django.db import models

class Usuarios(models.Model):
    usuario = models.CharField(max_length=50)
    password  = models.CharField(max_length=50)

    
    def __str__(self):
        return self.usuario 
    



    # Create your models here.
