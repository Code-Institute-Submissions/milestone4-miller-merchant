# -*- coding: utf-8 -*-
# Generated by Django 1.11.17 on 2019-12-15 22:10
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bookreview', '0007_bookreview_vote'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bookreview',
            name='vote',
            field=models.IntegerField(default=0),
        ),
    ]