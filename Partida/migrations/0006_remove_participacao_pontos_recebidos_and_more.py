# Generated by Django 5.1.1 on 2024-12-07 14:12

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Partida', '0005_partida_qr_code'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.RemoveField(
            model_name='participacao',
            name='pontos_recebidos',
        ),
        migrations.AddConstraint(
            model_name='participacao',
            constraint=models.UniqueConstraint(fields=('usuario', 'partida'), name='unique_participacao'),
        ),
    ]
