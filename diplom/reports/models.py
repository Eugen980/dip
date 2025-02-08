from django.db import models


class Reports(models.Model):
    date = models.DateField(verbose_name="Дата")
    date_since = models.DateField(verbose_name='Дата начала периода')
    date_to = models.DateField(verbose_name='Дата конца периода')
# Create your models here.
