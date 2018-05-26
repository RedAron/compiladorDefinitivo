from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect, HttpResponse
from django.template import loader

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

def Usuario_detail(request, pk):
    usuarios = get_object_or_404(Usuario, pk=pk)
    template = loader.get_template('Usuario_detail.html')
    context = {
        'usuario': usuarios
    }

    return HttpResponse(template.render(context, request))
