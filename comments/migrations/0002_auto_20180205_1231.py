# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2018-02-05 12:31
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('comments', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='comment',
            options={'ordering': ['-created_time']},
        ),
    ]
