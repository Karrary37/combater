# Generated by Django 3.1.7 on 2021-03-31 12:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('combaterincendio', '0003_auto_20210330_2115'),
    ]

    operations = [
        migrations.CreateModel(
            name='Clientes',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('criados', models.DateField(auto_now_add=True, verbose_name='Criação')),
                ('modificado', models.DateField(auto_now=True, verbose_name='Atualização')),
                ('ativo', models.BooleanField(default=True, verbose_name='Ativo?')),
                ('nome', models.CharField(max_length=100, verbose_name='Nome')),
                ('empresa', models.CharField(max_length=100, verbose_name='Empresa')),
                ('comentario', models.TextField(max_length=200, verbose_name='Comentario')),
                ('estrelas', models.CharField(choices=[('<span><i class="lni-star-filled"></i></span> </span> <span><i class="lni-star-half"></i></span><span><i class="lni-star-half"></i></span> <span><i class="lni-star-half"></i></span> <span><i class="lni-star-half"></i></span>', 'Uma Estrela'), ('<span><i class="lni-star-filled"></i></span> <span><i class="lni-star-filled"></i></span> <span><i class="lni-star-half"></i> </span> <span><i class="lni-star-half"></i></span> <span><i class="lni-star-half"></i></span>', 'Duas Estrelas'), ('<span><i class="lni-star-filled"></i></span> <span><i class="lni-star-filled"></i></span> <span><i class="lni-star-filled"></i></span> <span><i class="lni-star-half"></i></span> <span><i class="lni-star-half"></i></span>', 'Três Estrela'), ('<span><i class="lni-star-filled"></i></span> <span><i class="lni-star-filled"></i></span> <span><i class="lni-star-filled"></i></span> <span><i class="lni-star-filled"></i></span> <span><i class="lni-star-half"></i></span>', 'Quatro Estrela'), ('<span><i class="lni-star-filled"></i></span> <span><i class="lni-star-filled"></i></span> <span><i class="lni-star-filled"></i></span> <span><i class="lni-star-filled"></i></span> <span><i class="lni-star-filled"></i></span>', 'Cinco Estrela')], max_length=250, verbose_name='Estrelas')),
                ('imagem', models.ImageField(upload_to='clientes', verbose_name='Foto')),
            ],
            options={
                'verbose_name': 'Cliente',
                'verbose_name_plural': 'Clientes',
            },
        ),
    ]
