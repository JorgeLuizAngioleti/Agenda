# Generated by Django 2.0.5 on 2018-05-04 19:48

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('meu', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='agenda',
            name='eletronico',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='meu.Aparelho'),
        ),
    ]