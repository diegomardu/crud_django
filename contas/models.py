from django.db import models
from django.db.models.deletion import CASCADE

# Create your models here.

class Categoria(models.Model):
    nome = models.CharField(max_length=200)
    data = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return self.nome

class Transacao(models.Model):
    nome = models.CharField(max_length=200)
    descricao = models.CharField(max_length=200)
    data = models.DateTimeField()
    valor = models.DecimalField(max_digits=7, decimal_places=2)
    categoria = models.ForeignKey(Categoria, on_delete=CASCADE)

    class Meta:
        verbose_name_plural = 'Transacoes'

    def __str__(self) -> str:
        return self.nome


