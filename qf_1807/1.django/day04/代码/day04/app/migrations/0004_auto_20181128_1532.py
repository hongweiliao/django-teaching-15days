# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-11-28 07:32
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0003_auto_20181127_1528'),
    ]

    operations = [
        migrations.AddField(
            model_name='student',
            name='shuxue',
            field=models.DecimalField(decimal_places=1, max_digits=3, null=True),
        ),
        migrations.AddField(
            model_name='student',
            name='yuwen',
            field=models.DecimalField(decimal_places=1, max_digits=3, null=True),
        ),
    ]
