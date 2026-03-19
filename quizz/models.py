from django.db import models

class Pergunta(models.Model):
    texto = models.CharField(max_length=255)
    opcao_a = models.CharField(max_length=100)
    opcao_b = models.CharField(max_length=100)
    opcao_c = models.CharField(max_length=100)
    opcao_d = models.CharField(max_length=100)
    resposta_correta = models.CharField(max_length=1)

    def __str__(self):
        return self.texto