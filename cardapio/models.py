from django.db import models
from django.contrib.auth.models import User
from datetime import date
from django.urls import reverse

# Create your models here.
class Cardapio(models.Model):
    pratoPrincipal = models.TextField(max_length=30)
    refeicao = models.TextField(max_length=30)
    salada = models.TextField(max_length=30)
    acompanhamento = models.TextField(max_length=30)
    sobremesa = models.TextField(max_length=30)
    observa = models.TextField(blank=True, null=True)
    dataCap = models.DateField(default=date.today)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def get_absolute_url(self):
        return reverse('home')

    def __str__(self):
        return self.pratoPrincipal

class Reserva(models.Model):
    resData = models.DateField(default=date.today)
    resHora = models.TimeField()
    idCap = models.ForeignKey(Cardapio, null=True, related_name='reserva', on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.resData

    def get_absolute_url(self):
        return reverse('home')