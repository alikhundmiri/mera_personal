# Generated by Django 2.2.1 on 2019-05-10 10:30

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('blogs', '0050_auto_20180418_1453'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='publish',
            field=models.DateField(default=datetime.datetime(2019, 5, 10, 10, 30, 48, 986369, tzinfo=utc)),
        ),
    ]
