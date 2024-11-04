from django.db import models

class Linha(models.Model):
    numero = models.CharField(max_length=10, unique=True)
    descricao = models.CharField(max_length=200)

    def __str__(self):
        return self.numero

class Onibus(models.Model):
    capacidade_sentados = models.IntegerField()
    numero = models.CharField(max_length=10)
    capacidade_em_pe = models.IntegerField()
    linha = models.ForeignKey(Linha, on_delete=models.CASCADE, related_name='onibuss', null=True)  # Torne o campo 'linha' nulo

    def __str__(self):
        return self.numero

class Rota(models.Model):
    nome = models.CharField(max_length=100)
    ponto_inicio = models.CharField(max_length=100, default='Ponto de Início Padrão')  # Adiciona um valor padrão
    ponto_fim = models.CharField(max_length=100, default='Ponto de Fim Padrão')

    def __str__(self):
        return self.nome  # Corrigi para usar o atributo correto 'nome'


class PontoOnibus(models.Model):
    nome = models.CharField(max_length=100)
    latitude = models.FloatField()
    longitude = models.FloatField()
    linhas = models.ManyToManyField(Linha, related_name='pontos_onibus')

    def __str__(self):
        return self.nome
