# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2016-09-20 09:47
from __future__ import unicode_literals

import ckeditor.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('iCHD', '0006_comment_datetime'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blog',
            name='body',
            field=ckeditor.fields.RichTextField(verbose_name='文章内容'),
        ),
    ]
