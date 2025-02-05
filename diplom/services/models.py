from django.db import models


class Services(models.Model):
    date = models.DateField(blank="True", verbose_name="Дата")
    name = models.CharField(max_length=250, verbose_name='Наименование')
    description = models.TextField(max_length=250, verbose_name='Описание')
    price = models.IntegerField(verbose_name='Стоимость')
    unit = models.IntegerField(verbose_name='Единица измерения')
# Create your models here.
