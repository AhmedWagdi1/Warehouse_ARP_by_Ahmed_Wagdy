# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2018-10-19 19:23
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0053_auto_20181019_2109'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='farm',
            name='farm_company',
        ),
    ]