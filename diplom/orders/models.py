from django.db import models

from diplom.clients.models import Clients
from diplom.manager import models as m

class Orders(models.Model):
    date = models.DateField(blank="True", verbose_name="Дата")
    client = models.ForeignKey(Clients, on_delete=models.DO_NOTHING, verbose_name="Клиент")
    executor = models.ForeignKey(m.Executors, on_delete=models.DO_NOTHING, verbose_name="Исполнитель")
    agreement_date = models.DateField(verbose_name="Дата договора")
    account_number = models.IntegerField(verbose_name="Номер счёта")
    act_date = models.DateField(verbose_name="Дата акта")
    summa = models.IntegerField(verbose_name="Сумма")
    amount = models.IntegerField(verbose_name="Количество")
    contract_data = models.CharField(max_length=250, verbose_name="Данные контракта")
    act_data = models.CharField(max_length=250, verbose_name="Данные акта")
