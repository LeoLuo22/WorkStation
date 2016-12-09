# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2016-12-09 09:46
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('HouseRent', '0012_merge_20161209_1745'),
    ]

    operations = [
        migrations.AddField(
            model_name='house',
            name='isMedium',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='house',
            name='name',
            field=models.CharField(default='default', max_length=50),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='house',
            name='username',
            field=models.CharField(default='default', max_length=50),
            preserve_default=False,
        ),
    ]
