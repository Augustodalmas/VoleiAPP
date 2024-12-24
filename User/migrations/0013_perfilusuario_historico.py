# Generated by Django 5.1.1 on 2024-12-11 09:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Partida', '0007_historicopartida'),
        ('User', '0012_alter_perfilusuario_cpf'),
    ]

    operations = [
        migrations.AddField(
            model_name='perfilusuario',
            name='historico',
            field=models.ManyToManyField(blank=True, related_name='usuarios', to='Partida.historicopartida'),
        ),
    ]
