# Generated by Django 5.1.5 on 2025-02-05 17:41

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('manager', '0002_alter_requests_client_delete_clients'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Services',
        ),
    ]
