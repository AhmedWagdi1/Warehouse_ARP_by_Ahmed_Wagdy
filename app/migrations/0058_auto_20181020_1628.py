# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2018-10-20 14:28
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0057_daily_is_invoice'),
    ]

    operations = [
        migrations.AddField(
            model_name='client',
            name='client_mobile_number',
            field=models.IntegerField(default=1),
        ),
        migrations.AddField(
            model_name='supplier',
            name='supplier_mob_number',
            field=models.IntegerField(default=1),
        ),
    ]