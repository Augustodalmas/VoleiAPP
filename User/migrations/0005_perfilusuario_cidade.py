# Generated by Django 5.1.1 on 2024-11-20 23:40

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('User', '0004_cidade'),
    ]

    operations = [
        migrations.AddField(
            model_name='perfilusuario',
            name='cidade',
            field=models.ForeignKey(
                default=1, on_delete=django.db.models.deletion.CASCADE, to='User.cidade'),
        ),
    ]
