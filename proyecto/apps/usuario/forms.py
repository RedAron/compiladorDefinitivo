from apps.usuario.models import Usuario
from django.contrib.auth.forms import UserCreationForm

class UsuarioForm(UserCreationForm):

    class Meta:
        model = Usuario
        fields = [
                'username',
                'first_name',
                'last_name',
                'email',
                'edad',
                'ciudad',
                'pais',
                'lenguaje',
            ]
        labels = {
                'username' : 'Nombre de usuario',
                'first_name' : 'Nombre',
                'last_name' : 'Apellido',
                'email' : 'Correo',
                'edad' : 'Edad',
                'ciudad' : 'Ciudad',
                'pais' : 'Pais',
                'lenguaje' : 'Lenguaje',
            }