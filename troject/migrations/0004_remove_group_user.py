# -*- coding: utf-8 -*-
# Generated by Django 1.11.18 on 2019-01-22 07:46
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('troject', '0003_auto_20190121_2040'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='group',
            name='user',
        ),
    ]