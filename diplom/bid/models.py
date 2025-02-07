from django.db import models

from diplom.clients.models import Clients
from diplom.services.models import Services


class Bid(models.Model):
    date = models.DateField(verbose_name='Дата')
    name = models.CharField(max_length=250, verbose_name='Название')
    description = models.TextField(max_length=250, verbose_name='Описание')
    phone = models.CharField(max_length=250, verbose_name='Телефон')
    email = models.EmailField(verbose_name='Почта')
    client = models.ForeignKey(Clients, on_delete=models.PROTECT, verbose_name='Клиент')
    service = models.ForeignKey(Services, on_delete=models.PROTECT, verbose_name='Услуга')

    def __str__(self):
        return self.name
