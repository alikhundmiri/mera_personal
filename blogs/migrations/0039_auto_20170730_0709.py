# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-07-30 07:09
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('blogs', '0038_auto_20170730_0708'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='publish',
            field=models.DateField(default=datetime.datetime(2017, 7, 30, 7, 8, 59, 856871, tzinfo=utc)),
        ),
    ]