# Generated by Django 2.2 on 2019-04-23 14:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ambiental', '0002_auto_20190423_1123'),
    ]

    operations = [
        migrations.AlterField(
            model_name='propriedade',
            name='areaTotal',
            field=models.DecimalField(decimal_places=1, max_digits=5),
        ),
    ]