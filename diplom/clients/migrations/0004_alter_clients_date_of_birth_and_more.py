# Generated by Django 5.1.5 on 2025-02-08 20:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('clients', '0003_alter_clients_bank'),
    ]

    operations = [
        migrations.AlterField(
            model_name='clients',
            name='date_of_birth',
            field=models.DateTimeField(verbose_name='Дата рождения'),
        ),
        migrations.AlterField(
            model_name='clients',
            name='passports_number',
            field=models.IntegerField(verbose_name='Номер паспорта'),
        ),
        migrations.AlterField(
            model_name='clients',
            name='passports_series',
            field=models.IntegerField(verbose_name='Серия паспорта'),
        ),
        migrations.AlterField(
            model_name='clients',
            name='phone',
            field=models.CharField(max_length=14, verbose_name='Номер телефона'),
        ),
    ]
