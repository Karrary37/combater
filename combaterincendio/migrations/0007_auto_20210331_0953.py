# Generated by Django 3.1.7 on 2021-03-31 12:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('combaterincendio', '0006_auto_20210331_0949'),
    ]

    operations = [
        migrations.AlterField(
            model_name='clientes',
            name='imagem',
            field=models.ImageField(upload_to='clientes', verbose_name='Foto'),
        ),
    ]