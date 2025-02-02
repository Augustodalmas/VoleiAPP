# Generated by Django 5.1.1 on 2025-01-25 14:38

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Partida', '0013_remove_partida_pago_participacao_pago'),
    ]

    operations = [
        migrations.CreateModel(
            name='Local',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=256)),
                ('cidade', models.CharField(max_length=256)),
                ('bairro', models.CharField(max_length=256)),
                ('rua', models.CharField(max_length=256)),
                ('numero', models.IntegerField()),
                ('CEP', models.CharField(max_length=9)),
            ],
        ),
        migrations.AlterField(
            model_name='partida',
            name='nivel',
            field=models.CharField(choices=[('Iniciante', 'Iniciante'), ('Intermediário', 'Intermediário'), ('Avançado', 'Avançado')], default='Iniciante', max_length=15),
        ),
        migrations.AlterField(
            model_name='partida',
            name='local',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='Quadra_jogo', to='Partida.local'),
        ),
    ]
