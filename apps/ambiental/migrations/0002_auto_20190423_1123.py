# Generated by Django 2.2 on 2019-04-23 14:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ambiental', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='propriedade',
            name='areaReserva',
            field=models.DecimalField(blank=True, decimal_places=5, max_digits=5, null=True),
        ),
        migrations.AlterField(
            model_name='propriedade',
            name='areaTotal',
            field=models.DecimalField(decimal_places=5, max_digits=5),
        ),
    ]
