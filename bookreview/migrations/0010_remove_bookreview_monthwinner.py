# -*- coding: utf-8 -*-
# Generated by Django 1.11.17 on 2020-01-21 21:49
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('bookreview', '0009_bookreview_monthwinner'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='bookreview',
            name='monthwinner',
        ),
    ]