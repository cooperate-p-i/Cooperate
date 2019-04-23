# Generated by Django 2.2 on 2019-04-23 14:08

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('pessoal', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Cultura',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=50)),
                ('tipo', models.CharField(max_length=20)),
                ('areaPlantada', models.DecimalField(decimal_places=2, max_digits=5)),
            ],
        ),
        migrations.CreateModel(
            name='Rebanho',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tipo', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='Propriedade',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=100)),
                ('areaTotal', models.DecimalField(decimal_places=2, max_digits=5)),
                ('areaReserva', models.DecimalField(blank=True, decimal_places=2, max_digits=5, null=True)),
                ('culturaPrimaria', models.ManyToManyField(to='ambiental.Cultura')),
                ('proprietario', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='pessoal.Familia')),
                ('rebanho1', models.ManyToManyField(to='ambiental.Rebanho')),
            ],
        ),
    ]
