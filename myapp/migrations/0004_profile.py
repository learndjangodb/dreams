# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2016-12-22 11:36
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0003_auto_20161222_1618'),
    ]

    operations = [
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('picture', models.ImageField(upload_to='pictures')),
            ],
            options={
                'db_table': 'profile',
            },
        ),
    ]
