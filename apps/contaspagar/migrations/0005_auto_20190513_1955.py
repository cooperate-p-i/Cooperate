# Generated by Django 2.2 on 2019-05-13 22:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contaspagar', '0004_contaspagar_parcela_atual'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contaspagar',
            name='data_pagar',
            field=models.DateField(blank=True, null=True),
        ),
    ]