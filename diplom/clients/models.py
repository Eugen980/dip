from django.db import models


class Clients(models.Model):
    date = models.DateTimeField(auto_now_add=True)
    last_name = models.CharField(max_length=250, verbose_name='Фамилия')
    first_name = models.CharField(max_length=250, verbose_name='Имя')
    patronymic = models.CharField(max_length=250, verbose_name='Отчетство')
    legal_adress = models.CharField(max_length=250, verbose_name='Адресс прописки')
    physical_adress = models.CharField(max_length=250, verbose_name='Фактический адресс')
    inn = models.IntegerField()
    kpp = models.IntegerField()
    bank = models.IntegerField()
    phone = models.CharField(max_length=14)
    email = models.EmailField()
    date_of_birth = models.DateTimeField()
    passports_series = models.IntegerField()
    passports_number = models.IntegerField()
    services = models.IntegerField()
    user_state = models.IntegerField()
