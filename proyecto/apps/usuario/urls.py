from django.conf.urls import url

from apps.usuario.views import *
from . import views


urlpatterns = [
	url(r'^$', welcome, name="welcome"),
    url(r'^home/diagrama/$', diagramas, name="diagrama"),
    url(r'^registro', RegistroUsuario.as_view(), name="registro"),
    
    url(r'^usuario/editar/(?P<pk>\d+)$', actualizarUsuario.as_view(), name='editar'),
    url(r'^usuario/borrar/(?P<pk>\d+)$', eliminarUsuario.as_view(), name='eliminar'),

]
