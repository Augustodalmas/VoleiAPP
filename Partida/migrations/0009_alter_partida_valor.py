# Generated by Django 5.1.1 on 2024-12-23 16:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Partida', '0008_partida_id_stripe_partida_preco_stripe_partida_valor'),
    ]

    operations = [
        migrations.AlterField(
            model_name='partida',
            name='valor',
            field=models.DecimalField(decimal_places=2, default=10, max_digits=10),
        ),
    ]
