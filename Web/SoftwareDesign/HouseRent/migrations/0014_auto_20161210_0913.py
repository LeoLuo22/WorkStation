# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2016-12-10 01:13
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('HouseRent', '0013_auto_20161209_1746'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='idpic',
            field=models.CharField(default='', max_length=100),
        ),
        migrations.AddField(
            model_name='user',
            name='owner',
            field=models.CharField(default='', max_length=16),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='user',
            name='paper',
            field=models.CharField(default='', max_length=16),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='user',
            name='paperpic',
            field=models.CharField(default='', max_length=100),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='user',
            name='taxpaper',
            field=models.CharField(default='', max_length=16),
            preserve_default=False,
        ),
    ]
