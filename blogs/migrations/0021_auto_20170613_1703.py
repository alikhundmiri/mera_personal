# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-06-13 17:03
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('blogs', '0020_auto_20170613_1625'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='publish',
            field=models.DateField(default=datetime.datetime(2017, 6, 13, 17, 3, 19, 405869, tzinfo=utc)),
        ),
    ]
