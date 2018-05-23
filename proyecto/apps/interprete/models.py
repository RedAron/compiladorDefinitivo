from django.db import models

# Create your models here.
from apps.usuario.models import Usuario
import datetime


# Create your models here.

class Programa(models.Model):
   
    nombre=models.CharField(max_length=30)
    script=models.TextField()
    tiempo=models.DateField(("Date"),default=datetime.date.today)
    usuario=models.ForeignKey(Usuario,on_delete=models.CASCADE)
    
