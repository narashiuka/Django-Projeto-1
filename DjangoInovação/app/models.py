"""
Definition of models.
"""

from django.db import models
from django.contrib.auth.models import User

class Evento(models.Model):
    titulo = models.CharField(max_length=100)
    descricao = models.TextField(blank=True, null=True)
    data_evento = models.DateTimeField(verbose_name='Data do Evento')
    data_criacao = models.DateTimeField(auto_now=True)
    texto = models.TextField(blank=True, null=True)
    Usuario = models.ForeignKey(User, on_delete=models.CASCADE)
    local = models.TextField(blank=True, null=True, default='')

    class Meta:
        db_table = 'Evento'

    def __str__(self):
        return self.titulo

    def pegando_data_convertida(self):
        return self.data_evento.strftime('%d/%m/%Y  %H:%M')

    def get_data_input_evento(self):
        return self.data_evento.strftime('%Y-%m-%dT%H:%M')

