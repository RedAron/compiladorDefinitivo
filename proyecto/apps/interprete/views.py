from django.shortcuts import render
from django.http import HttpResponseRedirect, HttpResponse

from apps.interprete.models import Programa
from django.http import JsonResponse
from .models import Programa
from django.contrib.auth.models import User
from .forms import programaForm
from django.template import loader
from django.core.urlresolvers import reverse_lazy


# Create your views here.

def compilador(request):
    return render(request, 'interprete/compilador.html')

def guardar(request):
    model = Programa
    template_name = 'interprete/compilador.html'
    form_class = programaForm
    success_url = reverse_lazy('compilador')