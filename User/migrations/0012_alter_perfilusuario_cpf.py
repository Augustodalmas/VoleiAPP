# Generated by Django 5.1.1 on 2024-11-23 14:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('User', '0011_perfilusuario_foto'),
    ]

    operations = [
        migrations.AlterField(
            model_name='perfilusuario',
            name='cpf',
            field=models.CharField(
                blank=True, default='000.000.000-00', max_length=14),
        ),
    ]
