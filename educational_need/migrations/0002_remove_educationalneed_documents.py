# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-06-22 18:39
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('educational_need', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='educationalneed',
            name='documents',
        ),
    ]