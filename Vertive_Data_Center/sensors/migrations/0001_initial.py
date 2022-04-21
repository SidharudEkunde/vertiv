# Generated by Django 3.1.6 on 2022-03-29 09:10

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('system', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='IAQ',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('macid', models.CharField(max_length=40, unique=True)),
                ('co2', models.FloatField()),
                ('tvoc', models.FloatField()),
                ('x', models.FloatField()),
                ('y', models.FloatField()),
                ('room', models.CharField(max_length=100)),
                ('lastseen', models.DateTimeField(auto_now=True)),
                ('battery', models.FloatField()),
            ],
        ),
        migrations.CreateModel(
            name='TemperatureHumidity',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('macid', models.CharField(db_index=True, max_length=50, unique=True)),
                ('temperature', models.FloatField()),
                ('lastseen', models.DateTimeField(auto_now=True)),
                ('battery', models.FloatField()),
                ('systemid', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='system.system')),
            ],
        ),
        migrations.CreateModel(
            name='WeeklyTemperatureHumidity',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('temperature', models.FloatField()),
                ('timestamp', models.DateTimeField(auto_now=True)),
                ('asset', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='sensors.temperaturehumidity')),
            ],
        ),
        migrations.CreateModel(
            name='MonthlyTemperatureHumidity',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('temperature', models.FloatField()),
                ('timestamp', models.DateTimeField(auto_now=True)),
                ('asset', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='sensors.temperaturehumidity')),
            ],
        ),
        migrations.CreateModel(
            name='DailyTemperatureHumidity',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('temperature', models.FloatField()),
                ('timestamp', models.DateTimeField(auto_now=True)),
                ('asset', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='sensors.temperaturehumidity')),
            ],
        ),
    ]
