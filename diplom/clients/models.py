from django.db import models

from diplom.services.models import Services
from diplom.manager.models import Status, Bank

class Clients(models.Model):
    date = models.DateTimeField(auto_now_add=True)
    last_name = models.CharField(max_length=250, verbose_name='Фамилия')
    first_name = models.CharField(max_length=250, verbose_name='Имя')
    patronymic = models.CharField(max_length=250, verbose_name='Отчетство')
    legal_adress = models.CharField(max_length=250, verbose_name='Адресс прописки')
    physical_adress = models.CharField(max_length=250, verbose_name='Фактический адресс')
    inn = models.IntegerField()
    kpp = models.IntegerField()
    bank =models.ForeignKey(Bank, on_delete=models.DO_NOTHING, verbose_name='Банк')
    phone = models.CharField(max_length=14)
    email = models.EmailField()
    date_of_birth = models.DateTimeField()
    passports_series = models.IntegerField()
    passports_number = models.IntegerField()
    services = models.ForeignKey(Services, on_delete=models.DO_NOTHING, verbose_name='Услуги')
    user_state = models.ForeignKey(Status, on_delete=models.DO_NOTHING, verbose_name='Статус')

    def get_full_name(self):
        return f'{self.last_name} {self.first_name} {self.patronymic}' 

    def __str__(self):
        return self.get_full_name()