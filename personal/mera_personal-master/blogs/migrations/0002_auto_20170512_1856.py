# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-05-12 18:56
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('blogs', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='publish',
            field=models.DateField(default=datetime.datetime(2017, 5, 12, 18, 56, 52, 990919, tzinfo=utc)),
        ),
    ]
