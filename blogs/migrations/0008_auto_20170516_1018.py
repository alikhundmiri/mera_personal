# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-05-16 10:18
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('blogs', '0007_auto_20170516_1017'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='publish',
            field=models.DateField(default=datetime.datetime(2017, 5, 16, 10, 18, 6, 626934, tzinfo=utc)),
        ),
    ]
