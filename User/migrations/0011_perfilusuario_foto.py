# Generated by Django 5.1.1 on 2024-11-23 13:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('User', '0010_alter_perfilusuario_rotacao'),
    ]

    operations = [
        migrations.AddField(
            model_name='perfilusuario',
            name='foto',
            field=models.ImageField(blank=True, null=True, upload_to='perfil_imagens/'),
        ),
    ]
