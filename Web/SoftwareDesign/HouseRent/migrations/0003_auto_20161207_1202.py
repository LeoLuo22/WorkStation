# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2016-12-07 04:02
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('HouseRent', '0002_mediumhouse_normlhouse'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='NormlHouse',
            new_name='NormalHouse',
        ),
    ]
