# Generated by Django 2.2 on 2019-05-14 03:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ambiental', '0015_auto_20190513_2357'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cultura',
            name='areaPlantada',
            field=models.DecimalField(decimal_places=1, max_digits=11),
        ),
        migrations.AlterField(
            model_name='propriedade',
            name='areaReserva',
            field=models.DecimalField(blank=True, decimal_places=1, max_digits=16, null=True),
        ),
        migrations.AlterField(
            model_name='propriedade',
            name='areaTotal',
            field=models.DecimalField(decimal_places=1, max_digits=16),
        ),
    ]