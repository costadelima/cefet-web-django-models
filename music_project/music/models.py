from django.db import models

# Create your models here.

class Musico(models.Model):
    first_name = models.CharField(max_length = 50)
    last_name = models.CharField(max_length = 50)
    instrument = models.CharField(max_length = 50)
    idade = models.IntegerField()

    def __str__(self):
        return self.first_name


class EstiloMusical(models.Model):
    estilo = models.CharField(max_length = 50)

    def __str__(self):
        return self.estilo


class Banda(models.Model):
    nome = models.CharField(max_length = 50)
    criaçao = models.DateField()
    estilo = models.ForeignKey(EstiloMusical,on_delete = models.PROTECT)
    musico = models.ManyToManyField(Musico)

    def __str__(self):
        return self.nome
