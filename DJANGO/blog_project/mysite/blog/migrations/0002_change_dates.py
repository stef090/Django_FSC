# -*- coding: utf-8 -*-
# Generated by Django 1.11.8 on 2017-12-08 14:49
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_add_posts_comments'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='create_date',
            field=models.DateTimeField(default=datetime.datetime(2017, 12, 8, 14, 49, 31, 539005, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='post',
            name='create_date',
            field=models.DateTimeField(default=datetime.datetime(2017, 12, 8, 14, 49, 31, 538464, tzinfo=utc)),
        ),
    ]