# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-07-14 14:28
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('blogs', '0026_auto_20170615_1605'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='publish',
            field=models.DateField(default=datetime.datetime(2017, 7, 14, 14, 28, 38, 676202, tzinfo=utc)),
        ),
    ]