# Generated by Django 4.1 on 2022-09-27 01:48

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todolist', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='task',
            name='is_finished',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='task',
            name='date',
            field=models.DateField(default=datetime.datetime(2022, 9, 27, 8, 48, 2, 520811)),
        ),
    ]
