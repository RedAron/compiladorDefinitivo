from django.conf.urls import url

from apps.usuario.views import *
from . import views

urlpatterns = [
	url(r'^$', welcome, name="welcome"),
    url(r'^registro', RegistroUsuario.as_view(), name="registro"),
    

]
