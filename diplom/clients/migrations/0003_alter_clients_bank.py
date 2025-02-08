# Generated by Django 5.1.5 on 2025-02-08 17:50

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('clients', '0002_alter_clients_services_alter_clients_user_state'),
        ('manager', '0002_bank'),
    ]

    operations = [
        migrations.AlterField(
            model_name='clients',
            name='bank',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='manager.bank', verbose_name='Банк'),
        ),
    ]
