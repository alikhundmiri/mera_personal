# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-07-24 08:23
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('blogs', '0029_auto_20170723_2041'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='publish',
            field=models.DateField(default=datetime.datetime(2017, 7, 24, 8, 23, 28, 757642, tzinfo=utc)),
        ),
    ]
