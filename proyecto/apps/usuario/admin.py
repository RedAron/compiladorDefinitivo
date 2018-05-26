from django.contrib import admin

# Register your models here.
from apps.usuario.models import Usuario


@admin.register(Usuario)
class adminUsuario(admin.ModelAdmin):
    list_display=('username',)

