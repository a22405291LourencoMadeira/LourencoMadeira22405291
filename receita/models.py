from django.db import models

class Receita(models.Model):
    nome = models.CharField(max_length=150)
    descricao = models.TextField()
    tempo_preparo = models.IntegerField()

    def __str__(self):
        return f'{self.nome} ({self.tempo_preparo} min)'