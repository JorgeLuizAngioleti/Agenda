# Generated by Django 2.0.5 on 2018-05-07 22:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('meu', '0009_auto_20180505_1639'),
    ]

    operations = [
        migrations.AlterField(
            model_name='agenda',
            name='aula',
            field=models.CharField(default='1m', max_length=2, verbose_name='Aula'),
        ),
    ]