# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2016-12-22 10:48
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0002_auto_20161222_1045'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='dreamreal',
            options={'ordering': ('name',)},
        ),
    ]
