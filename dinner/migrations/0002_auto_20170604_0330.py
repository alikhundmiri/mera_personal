# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-06-04 03:30
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dinner', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='dishes',
            name='name',
            field=models.TextField(max_length=100, unique=True),
        ),
    ]
