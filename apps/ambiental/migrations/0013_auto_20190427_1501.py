# Generated by Django 2.2 on 2019-04-27 18:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ambiental', '0012_auto_20190427_1450'),
    ]

    operations = [
        migrations.AlterField(
            model_name='propriedade',
            name='areaReserva',
            field=models.DecimalField(blank=True, decimal_places=1, max_digits=10, null=True),
        ),
        migrations.AlterField(
            model_name='propriedade',
            name='areaTotal',
            field=models.DecimalField(decimal_places=1, max_digits=10),
        ),
    ]
