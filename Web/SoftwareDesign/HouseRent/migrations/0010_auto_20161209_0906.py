# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2016-12-09 01:06
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('HouseRent', '0009_house_iswanted'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='house',
            name='isChecked',
        ),
        migrations.AddField(
            model_name='user',
            name='isChecked',
            field=models.BooleanField(default=True),
        ),
    ]