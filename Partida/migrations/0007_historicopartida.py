# Generated by Django 5.1.1 on 2024-12-11 09:51

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Partida', '0006_remove_participacao_pontos_recebidos_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='HistoricoPartida',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('data', models.DateField()),
                ('participacao', models.BooleanField(default=False)),
                ('partida', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='historicos', to='Partida.partida')),
            ],
        ),
    ]
