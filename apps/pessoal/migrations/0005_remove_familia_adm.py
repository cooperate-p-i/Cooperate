# Generated by Django 2.2 on 2019-04-25 00:36

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pessoal', '0004_familia_adm'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='familia',
            name='adm',
        ),
    ]
