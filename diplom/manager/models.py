from django.db import models


from django.db import models

class Clients(models.Model):
    date = models.DateTimeField(auto_now_add=True)
    last_name = models.CharField(max_length=250, verbose_name='last_name')
    first_name = models.CharField(max_length=250, verbose_name='name')
    patronymic = models.CharField(max_length=250, verbose_name='patronymic')
    legal_adress = models.CharField(max_length=250, verbose_name='legal_adress')
    physical_adress = models.CharField(max_length=250, verbose_name='physical_adress')
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

class Requests(models.Model):
    date = models.DateField(auto_now_add=True)
    name = models.CharField(max_length=250, verbose_name='name')
    description = models.TextField(max_length=250)
    phone = models.CharField(max_length=250)
    email = models.EmailField()
    client = models.ForeignKey('Clients', on_delete=models.PROTECT)
    service = models.CharField(max_length=250)

class Services(models.Model):
    date = models.DateField()
    name = models.CharField(max_length=250)
    description = models.TextField(max_length=250)
    price = models.IntegerField()
    unit = models.IntegerField()

# Create your models here.
