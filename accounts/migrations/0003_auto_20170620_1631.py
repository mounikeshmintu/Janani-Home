# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-06-20 14:31
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0002_auto_20170620_1626'),
    ]

    operations = [
        migrations.RenameField(
            model_name='profile',
            old_name='bio',
            new_name='about',
        ),
    ]