# Generated by Django 5.1.1 on 2024-12-23 17:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Partida', '0009_alter_partida_valor'),
    ]

    operations = [
        migrations.AddField(
            model_name='partida',
            name='pago',
            field=models.BooleanField(default=False),
        ),
    ]
