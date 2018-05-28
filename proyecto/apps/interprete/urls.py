from django.conf.urls import url

from apps.interprete.views import *

urlpatterns = [
	url(r'^compilador/$', guardar.as_view(), name="compilador"),
   
]