# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2016-12-11 01:30
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('HouseRent', '0015_auto_20161210_1447'),
    ]

    operations = [
        migrations.AddField(
            model_name='house',
            name='isBooked',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='user',
            name='bookedhouse',
            field=models.IntegerField(default=0),
        ),
    ]
