# Generated by Django 2.2.1 on 2019-05-11 16:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contaspagar', '0003_contaspagar_numero_parcela_total'),
    ]

    operations = [
        migrations.AddField(
            model_name='contaspagar',
            name='parcela_atual',
            field=models.CharField(blank=True, max_length=30, null=True),
        ),
    ]
