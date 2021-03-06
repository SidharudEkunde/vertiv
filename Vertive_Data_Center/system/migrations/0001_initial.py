# Generated by Django 3.1.6 on 2022-03-29 09:10

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='System',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=40, unique=True)),
                ('sysid', models.IntegerField()),
                ('image', models.ImageField(upload_to='static/tracking/')),
                ('capacity', models.IntegerField(default=3)),
            ],
        ),
    ]
