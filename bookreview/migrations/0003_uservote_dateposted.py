# -*- coding: utf-8 -*-
# Generated by Django 1.11.17 on 2019-11-14 23:10
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('bookreview', '0002_auto_20191103_2149'),
    ]

    operations = [
        migrations.AddField(
            model_name='uservote',
            name='dateposted',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]
