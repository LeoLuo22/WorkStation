# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2016-12-07 04:05
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('HouseRent', '0003_auto_20161207_1202'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mediumhouse',
            name='picpath',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='normalhouse',
            name='picpath',
            field=models.CharField(max_length=100),
        ),
    ]