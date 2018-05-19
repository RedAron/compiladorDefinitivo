from django.shortcuts import render
from django.http import HttpResponseRedirect, HttpResponse

from apps.usuario.models import Usuario
from django.contrib.auth.forms import UserCreationForm
from django.views.generic import CreateView
from django.core.urlresolvers import reverse_lazy

from apps.usuario.forms import UsuarioForm

def welcome(request):
	return render(request, 'usuario/welcome.html')

class RegistroUsuario(CreateView):
    model = Usuario
    template_name = 'usuario/registro.html'
    form_class = UsuarioForm
    success_url = reverse_lazy('login')