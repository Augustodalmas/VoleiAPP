# Generated by Django 5.1.1 on 2024-11-30 19:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Partida', '0002_partida_unique_partida'),
    ]

    operations = [
        migrations.AddField(
            model_name='partida',
            name='nivel',
            field=models.CharField(choices=[('Iniciante', 'Iniciante'), ('Intermediario', 'Intermediario'), ('Avancado', 'Avancado')], default='Iniciante', max_length=15),
        ),
        migrations.AddField(
            model_name='partida',
            name='rotacao',
            field=models.CharField(choices=[('5x1', '5x1'), ('6x0', '6x0'), ('4x2', '4x2')], default='6x0', max_length=3),
        ),
    ]
