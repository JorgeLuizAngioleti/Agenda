# Generated by Django 2.0.5 on 2018-05-14 17:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('meu', '0017_auto_20180513_1734'),
    ]

    operations = [
        migrations.AddField(
            model_name='aparelho',
            name='escola',
            field=models.CharField(default=1, max_length=50),
            preserve_default=False,
        ),
    ]
