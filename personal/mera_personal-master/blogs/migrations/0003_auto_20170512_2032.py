# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-05-12 20:32
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('blogs', '0002_auto_20170512_1856'),
    ]

    operations = [
        migrations.CreateModel(
            name='taggers',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tag_name', models.CharField(max_length=20)),
                ('tag_slug', models.SlugField(unique=True)),
                ('description', models.TextField(max_length=1000)),
            ],
            options={
                'ordering': ['-tag_name'],
            },
        ),
        migrations.AlterField(
            model_name='post',
            name='detail',
            field=models.TextField(max_length=23000),
        ),
        migrations.AlterField(
            model_name='post',
            name='publish',
            field=models.DateField(default=datetime.datetime(2017, 5, 12, 20, 32, 17, 447572, tzinfo=utc)),
        ),
        migrations.AddField(
            model_name='post',
            name='tags',
            field=models.ManyToManyField(to='blogs.taggers'),
        ),
    ]
