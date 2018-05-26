from django.conf.urls import url

from apps.interprete.views import compilador

urlpatterns = [
	url(r'^compilador/$', compilador, name="compilador"),
]