# Generated by Django 2.2 on 2019-04-29 15:03

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('cooperativa', '0001_initial'),
        ('pessoal', '0006_auto_20190427_1446'),
    ]

    operations = [
        migrations.AddField(
            model_name='familia',
            name='cooperativa',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.PROTECT, to='cooperativa.Cooperativa'),
            preserve_default=False,
        ),
    ]
