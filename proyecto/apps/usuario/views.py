from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect, HttpResponse
from django.template import loader

from apps.usuario.models import Usuario
from django.contrib.auth.forms import UserCreationForm
from django.views.generic import CreateView
from django.views.generic.edit import UpdateView
from django.views.generic.edit import DeleteView


from django.core.urlresolvers import reverse_lazy

from apps.usuario.forms import UsuarioForm
import json
def welcome(request):
    template=loader.get_template('usuario/welcome.html')
    context={
        'usuario':Usuario
    }
    return HttpResponse(template.render(context,request))

def diagramas(request):
    queryset=Usuario.objects.all()
    id= [obj.id for obj in queryset]
    pais= [obj.pais for obj in queryset]
    lenguaje= [obj.lenguaje for obj in queryset]
    aux=1
    for usuario1 in queryset:
        for usuario in queryset:
            if(usuario.pais==usuario1.pais):
                aux=aux+1
    aux2=1
    for usuario1 in queryset:
        for usuario in queryset:
            if(usuario1.lenguaje==usuario.lenguaje):
                aux2=aux2+1
    
    

        
    
    

    
    [obj.id for obj in queryset]

    context={
        'numpais':json.dumps(aux),
        'lenguaje':json.dumps(lenguaje),
        'numlenguaje':json.dumps(aux2),

        'pais': json.dumps(pais),
        'id':json.dumps(id)
    }
    return render(request,'usuario/estadisticas.html',context)




class RegistroUsuario(CreateView):
    model = Usuario
    template_name = 'usuario/registro.html'
    form_class = UsuarioForm
    success_url = reverse_lazy('login')

class actualizarUsuario(UpdateView):
    model=Usuario
    success_url=reverse_lazy('login')
    fields=['username',
                'first_name',
                'last_name',
                'email',
                'edad',
                'ciudad',
                'pais',
                'lenguaje',
            ]
class eliminarUsuario(DeleteView):
    template_name='usuario/eliminar.html'
    model=Usuario
    success_url=reverse_lazy('logout')


