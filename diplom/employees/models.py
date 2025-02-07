from django.db import models

from diplom.manager import models as m


class Emolyees(models.Model):
    last_name = models.CharField(max_length=250, verbose_name='Фамилия')
    first_name = models.CharField(max_length=250, verbose_name='Имя')
    patronymic = models.CharField(max_length=250, verbose_name='Отчетство')
    login = models.CharField(max_length=250, verbose_name='Логин')
    password = models.CharField(max_length=250, verbose_name='пароль')
    legal_adress = models.CharField(max_length=250, verbose_name='Адресс прописки')
    physical_adress = models.CharField(max_length=250, verbose_name='Фактический адресс')
    position = models.ForeignKey(m.Position,on_delete=models.DO_NOTHING, verbose_name='Должность')
    subdivision =  models.ForeignKey(m.Subdivision,on_delete=models.DO_NOTHING, verbose_name='Подразделение')
    role =  models.ForeignKey(m.Role,on_delete=models.DO_NOTHING, verbose_name='Роль')
    inn = models.IntegerField()
    snils = models.IntegerField()
    phone = models.CharField(max_length=14)
    email = models.EmailField()
    date_of_birth = models.DateField()
    passports_series = models.IntegerField(max_length=4)
    passports_number = models.IntegerField(max_length=6)
    date_of_employment = models.DateField(verbose_name='Дата принятия на работу')
    date_of_dismissal = models.DateField(null=True, verbose_name='Дата увольнения')
    education = models.CharField(max_length=250, verbose_name='Образование')
    salary = models.IntegerField(verbose_name='Оклад')

    def get_full_name(self):
        return f'{self.last_name} {self.first_name} {self.patronymic}' 

    def __str__(self):
        return self.get_full_name()