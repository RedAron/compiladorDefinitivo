from django.db import models

from django.contrib.auth.models import AbstractUser

class Usuario(AbstractUser):
	edad = models.CharField(max_length=50)
	ciudad = models.CharField(max_length=50)
	pais = models.CharField(max_length=50)
	lenguaje = models.CharField(max_length=50)
	
	

