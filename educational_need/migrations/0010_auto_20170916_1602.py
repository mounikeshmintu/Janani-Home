# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-09-16 14:02
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('educational_need', '0009_auto_20170912_2225'),
    ]

    operations = [
        migrations.AddField(
            model_name='educationalneed',
            name='hide_current_address',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='educationalneed',
            name='hide_permanent_address',
            field=models.BooleanField(default=False),
        ),
    ]
