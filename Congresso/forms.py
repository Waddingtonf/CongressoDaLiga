from Congresso.models import Frequencia
from django import forms
from django.forms import ModelForm


class FrequenciaForm(ModelForm):
        confirmacao = forms.CheckboxInput(attrs={'id': 'checkbox-1'})
        cursoparticipado_id = forms.IntegerField()
        aluno = forms.CharField()
        
        class Meta:
            model = Frequencia
            fields = ['confirma', 'aluno', 'cursoparticipado_id']


