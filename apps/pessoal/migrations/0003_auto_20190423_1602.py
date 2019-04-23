# Generated by Django 2.2 on 2019-04-23 19:02

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('pessoal', '0002_auto_20190423_1113'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='familia',
            name='administrador',
        ),
        migrations.AddField(
            model_name='membro',
            name='familia',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.PROTECT, to='pessoal.Familia'),
            preserve_default=False,
        ),
    ]