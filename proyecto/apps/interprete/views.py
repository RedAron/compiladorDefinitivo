from django.shortcuts import render
from django.http import HttpResponseRedirect, HttpResponse

from apps.interprete.models import *
# Create your views here.

def compilador(request):
    return render(request, 'usuario/compilador.html')
 
