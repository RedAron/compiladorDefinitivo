from django import forms
from .models import Programa

class programaForm(forms.ModelForm):
    class Meta:
        model=Programa

        fields = [
                'nombre',
                'script',
            ]
        labels = {
                'nombre' : 'Nombre de programa',
                'script' : 'script del programa',
            }
        def form_valid(self,form):
            self.object=form.save(commit=False)
            self.object.usuario=self.request.user
            self.object.save()
            return super(programaForm,self).form_valid(form)