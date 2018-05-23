from django.contrib import admin

# Register your models here.
from .models import Programa

@admin.register(Programa)
class adminPrograma(admin.ModelAdmin):
    list_display=('nombre','script','tiempo')

