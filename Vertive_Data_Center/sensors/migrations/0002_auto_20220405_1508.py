# Generated by Django 3.1.6 on 2022-04-05 15:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sensors', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='temperaturehumidity',
            name='max',
            field=models.FloatField(default=1),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='temperaturehumidity',
            name='min',
            field=models.FloatField(default=1),
            preserve_default=False,
        ),
    ]
