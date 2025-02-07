from django.db import models

from diplom.clients.models import Clients
from diplom.manager import models as m

class Charts(models.Model):
    date = models.DateField(verbose_name="Дата")
    subdivision = models.ForeignKey(m.Subdivision, on_delete=models.DO_NOTHING, verbose_name='Подразделение')
    date_since = models.DateField(verbose_name='Дата начала периода')
    date_to = models.DateField(verbose_name='Дата конца периода')
    charts_data = models.CharField(max_length=250, verbose_name='Описание графика')


    def __str__(self):
        return self.charts_data
