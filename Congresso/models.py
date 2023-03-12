from django.db import models
from django.conf import settings
from django.utils import timezone
from django.contrib.auth.models import User

# Create your models here.

class Cursos(models.Model):
    curso = models.CharField(max_length=64)
    data = models.DateField()
    diasemana = models.CharField(max_length=20)

class Frequencia(models.Model):
    cursoparticipado = models.ForeignKey(Cursos, on_delete=models.CASCADE)
    aluno = models.IntegerField()
    confirma = models.BooleanField()
    horario = models.DateTimeField(editable=False, default=timezone.now)

    